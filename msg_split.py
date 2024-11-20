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

    for child in soup.descendants:
        if isinstance(child, NavigableString):
            words = child.split()
            print('text', words)
        elif isinstance(child, Tag):
            print('tag', [str(child)])



def test():
    source = "<p>Hello, <b>world</b>!</p>"
    max_len = 10
    res = split_message(source, max_len)
    # for _ in res:
    #     print(_)


# Тестирование функции
def test():
    # source = "<p>Hello, <b>world</b>! This is a <i>test</i> message with <u>HTML</u> tags.</p>"
    source = "<p>Hello, <b>world</b>! This is a <i>long</i> message.</p>"
    max_len = 20
    res = split_message(source, max_len)
    for chunk in res:
        print(chunk)

if __name__ == "__main__":
    test()

    