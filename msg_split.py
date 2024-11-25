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


    # # go through html ver 1 - proplem to identificate the closing tag
    # for child in soup.recursiveChildGenerator():
    #     if isinstance(child, Tag):  # Обрабатываем тег
    #         print(process_tag(child))
    #     elif isinstance(child, NavigableString):
    #         print(process_text(child))

    # go through html - ver 2
    chunks = []
    len_tags = 0
    skipped_tags_count = 0
    chunk = ''
    for el in soup.descendants:
        if isinstance(el, Tag):
            if skipped_tags_count:
                skipped_tags_count -= 1
                continue
            tag_content = el.contents
            if not el.contents:  # Тег не содержит других элементов (например, <br>)
                print(f"Self-closing or empty tag: <{el.name}>")
                chunk += f'<{el.name}></{el.name}>'
                continue
            tags.append(el.name)
            chunk += f'<{el.name}>'
            for part in tag_content:
                if isinstance(part, Tag):
                    # check len
                    # if ok - add to chunk and raise skipped_counter
                    # if not - close all opened tags and return 1st chunk
                    # and start new chunk with current tag
                    print('curr part', part) # debug
                    for t in tags:
                        len_tags += len(f'</{t}>')
                    if len(chunk) + len_tags + len(part) < max_len:
                        chunk += str(part)
                        skipped_tags_count += 1
                    else:
                        for t in tags:
                            chunk += f'</{t}>'
                        chunks.append(chunk)
                        chunk = ''
                        for t in tags:
                            chunk += f'<{t}>'

                else: # should be str
                    # check len
                    # check len
                    # if ok - add to chunk
                    # if not - close all opened tags and return 1st chunk
                    # and start new chunk with current tag
                    print('curr part', part) # debug
                    for t in tags:
                        len_tags += len(f'</{t}>')
                    if len(chunk) + len_tags + len(part) <= max_len:
                        chunk += part
                    else:
                        for t in tags:
                            chunk += f'</{t}>'
                        chunks.append(chunk)
                        chunk = ''
                        for t in tags:
                            chunk += f'<{t}>'
                            continue
                    


        

        

# Тестирование
html = "<p>Hello, <b>world</b>!</p>" # total 27
template1 = "<p>Hello, <b>world</b>!</p>"
template2 = "<p>!</p>"
print(len(html), len(template1), len(template2))
max_len = 27

result = split_message(html, max_len)

for chunk in result:
    print(repr(chunk))  # Выводим сегменты





# if __name__ == "__main__":
#     test()

    