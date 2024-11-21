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
    chunk = ''
    tags = [] # list so that i can go through to form open and closing tags
    soup = BeautifulSoup(source, 'html.parser')

    def process_tag(tag):
        nonlocal chunk
        tag_name = tag.name
        tag_str = f'<{tag.name}>'
        tags_brackets_len = len(tag_name) * 2 + 5 # 2 tag names + <> + </>
        tags.append(tag.name)
        chunk_len = len(chunk)
        if tags_brackets_len + chunk_len <= max_len:
            chunk += tag_str
        return chunk


    # go through html
    for child in soup.recursiveChildGenerator():
        if isinstance(child, Tag):  # Обрабатываем тег
            print(process_tag(child))


# Тестирование
html = "<p>Hello, <b>world</b>!</p>"
max_len = 10

result = split_message(html, max_len)

for chunk in result:
    print(repr(chunk))  # Выводим сегменты





# if __name__ == "__main__":
#     test()

    