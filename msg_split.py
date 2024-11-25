from types import GeneratorType
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


MAX_LEN = 4096
BLOCK_TAGS = ["p", "b", "strong", "i", "ul", "ol", "div", "span"]


def split_message(source: str, max_len=MAX_LEN):# -> GeneratorType[str]:
    """
    Splits the original message (`source`) into fragments of the specified
    length (`max_len`)
    """
    # final list with all the chunks(fragments), in which orignal html is split
    # should include additional tags if needed
    chunks = []
    soup = BeautifulSoup(html, 'html.parser')
    tags = [] # opened tags
    words = []


    # cycle by every elem in html-doc
    for el in soup.descendants:
        print(el)
        if isinstance(el, Tag):
            # if tag is empty we can add it to curr chunk or raise error
            if not el.contents:
                print('empty tag')
                curr_tags = f'<{el.name}></{el.name}>'
                if len(curr_tags) + len(chunk) <= max_len:
                    chunk += curr_tags
                else:
                    print("Error: cannot close tag {el.name}")
                    break
            else:
                # start filling curr chunk
                chunk += f'<{el.name}>'
                tags.append(f'<{el.name}>')

                # go through all the content of current tag
                # it can be added totally or split into parts
                for content in el.contents:
                    print(content)
                    if isinstance(content, NavigableString):
                        len
                        if len(content) + len(chunk) + len_close_tags <= max_len:


        elif isinstance(el, NavigableString):
            words.append(str(el))
            

    print(tags)
    print(words)

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

    