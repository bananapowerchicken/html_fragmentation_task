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
    curr_fragment = []
    curr_fragment_len = 0
    open_tags_stack = []

    soup = BeautifulSoup(source, 'html.parser') # creates a tag-tree

    def extract_content(element):
        # Если элемент — текст, разбиваем его на слова
        if isinstance(element, NavigableString):
            words = str(element).split()  # Разделяем текст на слова
            return words
        elif isinstance(element, Tag):
            # Если элемент — тег, оставляем его как есть
            curr_str = str(element)
            end_tag_ind = curr_str.index('>')
            curr_tag = curr_str[:end_tag_ind+1]
            return [curr_tag]
        return []

    result = []
    for child in soup.descendants:  # Рекурсивно обходим все элементы
        result.extend(extract_content(child))

    return result



def test():
    source = "<p>Hello, <b>world</b>!</p>"
    max_len = 10
    res = split_message(source, max_len)
    # print()
    for item in res:
        print(repr(item))


# Тестирование функции
def test():
    source = "<p>Hello, <b>world</b>! This is a <i>test</i> message with <u>HTML</u> tags.</p>"
    # source = "<p>Hello, <b>world</b>! This is a <i>long</i> message.</p>"
    max_len = 20
    res = split_message(source, max_len)
    for chunk in res:
        print(chunk)

if __name__ == "__main__":
    test()

    