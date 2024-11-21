from bs4 import BeautifulSoup
from typing import Generator
from bs4.element import NavigableString, Tag

MAX_LEN = 100  # Для теста, можно поменять на 4096

def split_message(source: str, max_len=MAX_LEN) -> Generator[str, None, None]:
    soup = BeautifulSoup(source, "html.parser")
    
    current_chunk = ""  # Текущий фрагмент
    current_len = 0  # Длина текущего фрагмента
    open_tags = []  # Список открытых тегов
    closing_tags = []

    def add_opening_tags(tags):
        """Возвращает строку открывающих тегов."""
        return "".join(f"<{tag}>" for tag in tags)

    def add_closing_tags(tags):
        """Возвращает строку закрывающих тегов для всех открытых тегов."""
        return "".join(f"</{tag}>" for tag in reversed(tags))

    def process_text(text):
        """Обрабатывает текст, добавляя его в текущий фрагмент."""
        nonlocal current_chunk, current_len
        words = text.split()
        for word in words:
            # Проверяем, можем ли добавить слово, не превышая max_len
            if current_len + len(word) + 1 > max_len:  # +1 для пробела
                # Закрыть текущий фрагмент и начать новый
                yield current_chunk + add_closing_tags(open_tags)
                current_chunk = add_opening_tags(open_tags) + word
                current_len = len(current_chunk)
            else:
                if current_len > 0:
                    current_chunk += " "
                current_chunk += word
                current_len += len(word) + 1

    def process_tag(tag):
        """Обрабатывает добавление тегов в фрагмент."""
        nonlocal current_chunk, current_len, open_tags
        # tag_str = str(tag)
        tag_str = f"<{tag.name}>" # that is correct - adding only tag
        open_tags.append(tag.name)
        tmp = add_closing_tags(open_tags)
        # Проверяем, можем ли добавить тег, не превышая max_len
        if current_len + len(tag_str) + len(tmp) > max_len:
            # Закрыть текущий фрагмент и начать новый
            tmp = add_closing_tags(open_tags)
            print(len(tmp))
            yield current_chunk + add_closing_tags(open_tags)
            current_chunk = add_opening_tags(open_tags) + tag_str
            current_len = len(current_chunk)
        else:
            current_chunk += tag_str
            current_len += len(tag_str)

        # Обновляем список открытых тегов
        if not tag.is_empty_element:
            if tag.name not in open_tags:
                open_tags.append(tag.name)
            else:
                open_tags.remove(tag.name)

        # # my version
        # tmp = tag.contents
        # res = ''
        # for el in tmp:            
        #     res += str(el) # str content of current tag

        # tag_open = f"<{tag.name}>"
        # open_tags.append(tag_open)
        # tag_close = f"</{tag.name}>"
        # closing_tags.append(tag_close)
        # closing_tags.reverse()

        # if len()

       

    # Рекурсивно обрабатываем все элементы
    for child in soup.recursiveChildGenerator():
        if isinstance(child, NavigableString):  # Обрабатываем текст
            if child.strip():
                yield from process_text(child)  
        elif isinstance(child, Tag):  # Обрабатываем тег
            yield from process_tag(child)

    # Возвращаем последний фрагмент
    if current_chunk:
        yield current_chunk + add_closing_tags(open_tags)

# Пример использования
# html = "<p>Hello, <b>world</b>! This is a <i>test</i> message with <u>HTML</u> tags.</p><ul><li>Item 1</li><li>Item 2</li></ul>"
html = "<p>Hello, <b>world</b>!</p>"
max_len = 10

# Тестирование
for i, fragment in enumerate(split_message(html, max_len), 1):
    print(f"fragment #{i}: {len(fragment)} chars")
    print(fragment)
    print("-" * 40)
