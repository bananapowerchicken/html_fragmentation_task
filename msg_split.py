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
    full_chunk_len = 0
    tags = [] # list so that i can go through to form open and closing tags
    soup = BeautifulSoup(source, 'html.parser')

    def add_opening_tags(tags):
        """Возвращает строку открывающих тегов."""
        return "".join(f"<{tag}>" for tag in tags)

    def add_closing_tags(tags):
        """Возвращает строку закрывающих тегов для всех открытых тегов."""
        return "".join(f"</{tag}>" for tag in reversed(tags))

    def process_tag(tag):
        nonlocal chunk, full_chunk_len
        tag_name = tag.name
        tag_str = f'<{tag.name}>'
        tags.append(tag_name)

        tags_open = add_opening_tags(tags)
        tags_close = add_closing_tags(tags)
        all_tags_len = len(tags_open) + len(tags_close)
        tags.append(tag.name)
        len_chunk = len(chunk)
        if all_tags_len + len_chunk <= max_len: # if we can potentially close curr tag
            chunk += tag_str
            full_chunk_len = all_tags_len
        else:
            chunk += add_closing_tags
        return chunk
    
    def process_text(text):
        nonlocal chunk
        len_text = len(text)
        if len_text + full_chunk_len <= max_len:
            chunk += str(text)
        else:
            pass
        return chunk


    # go through html
    for child in soup.recursiveChildGenerator():
        if isinstance(child, Tag):  # Обрабатываем тег
            print(process_tag(child))
        elif isinstance(child, NavigableString):
            print(process_text(child))


# Тестирование
html = "<p>Hello, <b>world</b>!</p>"
max_len = 50

result = split_message(html, max_len)

for chunk in result:
    print(repr(chunk))  # Выводим сегменты





# if __name__ == "__main__":
#     test()

    