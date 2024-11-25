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


    def end_fragment():
        pass


    def end_fragment():
        pass


    def process_tag(el):
        nonlocal chunk, chunks

        # if tag is empty we can add it to curr chunk or raise error
        if not el.contents:
                print('empty tag')
                curr_tags = f'<{el.name}></{el.name}>'
                if len(curr_tags) + len(chunk) <= max_len:
                    chunk += curr_tags
                else:
                    print("Error: cannot close tag {el.name}")
        else:
            # start filling curr chunk
            chunk += f'<{el.name}>'
            tags.append(el.name)

            # working on inner elements of curr tag
            el_contents = el.contents # for debug
            for c in el_contents:
                print('c : ', c)
                if isinstance(c, Tag):            
                    process_tag(c, chunk)
                elif isinstance(c, NavigableString):
                    process_text(c)

    
    def process_text(el):
        print('processing text: ', el)
        closing_tags = generate_closing_tags(tags)
        curr_len = len(chunk) + len(closing_tags) + len(chunk)
        if curr_len <= max_len:
            chunk += str(el) + closing_tags
        else:
            print('Need to cut fragment')
            end_fragment()
            start_fragment()
            



    # cycle by every elem in html-doc
    for el in soup.descendants:
        print('el: ', el)
        if isinstance(el, Tag):            
            process_tag(el, chunk)
        elif isinstance(el, NavigableString):
            process_text(el)


        #         # go through all the content of current tag
        #         # it can be added totally or split into parts
        #         for content in el.contents:
        #             print(content)
        #             if isinstance(content, NavigableString):
        #                 # count len of closing tags for current moment to count total chunk len
        #                 len_close_tags = 0
        #                 for t in tags:
        #                     len_close_tags += len(f'</{t}>')

        #                 if len(content) + len(chunk) + len_close_tags <= max_len:
        #                     chunk += content
        #                 else:
        #                     # end chunk
        #                     for t in tags:
        #                         chunk += f'</{t}>'
        #                     chunks.append(chunk)
        #                     chunk = ''
        #                     break
        #             elif isinstance(content, Tag):
        #                 if not content.contents:
        #                     print('empty tag')
        #                     curr_tags = f'<{el.name}></{el.name}>'
        #                     if len(curr_tags) + len(chunk) <= max_len:
        #                         chunk += curr_tags
        #                     else:
        #                         print("Error: cannot close tag {el.name}")
        #                         break
        #                 else:
        #                     # start filling curr chunk
        #                     chunk += f'<{content.name}>'
        #                     tags.append(content.name)


        # elif isinstance(el, NavigableString):
        #     words.append(str(el))
            

    # print(tags)
    # print(words)

    return chunks



        

        

# Тестирование
html = "<p>Hello, <b>world</b>!</p>"      # total 27
template1 = "<p>Hello, <b>world</b>!</p>" # total 27
template2 = "<p>!</p>"                    # total 8
print(len(html), len(template1), len(template2))
max_len = 27

result = split_message(html, max_len)

for chunk in result:
    print(repr(chunk))  # Выводим сегменты





# if __name__ == "__main__":
#     test()

    