from types import GeneratorType
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


MAX_LEN = 4096
BLOCK_TAGS = ["p", "b", "strong", "i", "ul", "ol", "div", "span"]

def generate_closing_tags(tag_names):
    closing_tags = ''
    for t in tag_names:
        closing_tags += f'</{t}>'
    return closing_tags


def generate_opening_tags(tag_names):
    closing_tags = ''
    for t in tag_names:
        closing_tags += f'<{t}>'
    return closing_tags


def split_message(source: str, max_len=MAX_LEN):# -> GeneratorType[str]:
    """
    Splits the original message (`source`) into fragments of the specified
    length (`max_len`)
    """
    # final list with all the chunks(fragments), in which orignal html is split
    # should include additional tags if needed
    chunks = []
    chunk = ''
    soup = BeautifulSoup(html, 'html.parser')
    tags = [] # opened tags
    words = []


    def start_fragment():
        nonlocal chunk, chunks, tags
        print('Start fragment') # debug
        
        chunk = generate_opening_tags(tags)


    def end_fragment():
        nonlocal chunk, chunks, tags
        print('End fragment') # debug
        
        closing_tags = generate_closing_tags(tags)
        chunk += closing_tags
        print('Ended gragment: ', chunk)
        chunks.append(chunk)        




    def process_empty_tag():
        pass


    def process_tag(el):
        nonlocal chunk, chunks, tags
        
        print('Tag: ', el.name) # debug
        print('Tag contents: ', el.contents)

        # if len is ok
        # add to tags and append to chunk        
        # if len is more tha max len - end current fragment and start new one
        len_curr_tag = len(f'<{el.name}>') + len(f'</{el.name}>')
        len_chunk = len(chunk) # includes previous open tags
        len_closing_tags = len(generate_closing_tags(tags))

        if len_chunk + len_closing_tags + len_curr_tag <= max_len:
            tags.append(el.name)
            chunk += f'<{el.name}>'
        else:
            end_fragment()
            start_fragment()
        
        # need to process every item
        tag_content = el.contents
        for itm in tag_content:
            if isinstance(itm, NavigableString):
                process_text(itm)
            elif isinstance(itm, Tag):
                len_itm = len(str(itm))
                len_chunk = len(chunk)
                len_closing_tags = len(generate_closing_tags(tags))
                if len_chunk + len_closing_tags + len_itm <= max_len:
                    process_text(itm)
                else:
                    process_tag(itm)


    
    def process_text(el):
        nonlocal chunk, chunks, tags
        print('Text: ', el) # debug

        len_curr_text = len(str(el))
        len_chunk = len(chunk) # includes previous open tags
        len_closing_tags = len(generate_closing_tags(tags))

        if len_chunk + len_closing_tags + len_curr_text <= max_len:
            chunk += str(el)
        else:
            end_fragment()
            start_fragment()


            



    # cycle by every elem in html-doc
    for el in soup.descendants:
        print('-------------')
        print(f'el: ', el)
        if isinstance(el, Tag):
            process_tag(el)
        elif isinstance(el, NavigableString):
            process_text(el)        
      
    return chunks



        

        

# Тестирование
html = "<p>Hello, <b>world</b>!</p>"      # total 27
template1 = "<p>Hello, <b>world</b></p>"  # total 27
template2 = "<p>!</p>"                    # total 8
print(len(html), len(template1), len(template2))
max_len = 26

result = split_message(html, max_len)

for chunk in result:
    print(repr(chunk))  # Выводим сегменты





# if __name__ == "__main__":
#     test()

    