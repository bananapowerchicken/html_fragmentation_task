from types import GeneratorType
from bs4 import BeautifulSoup


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

    # print(soup.prettify())

    # recursively goes deep in inner tags    
    for el in soup.recursiveChildGenerator():
        tag = el.name
        t = el.text
        if isinstance(el, str):  # Если текст
            curr_text = el.strip()
        else:  # Если тег
            curr_text = el.text.strip()
        # curr_text = str(el)
        curr_text_len = len(curr_text)


        # finish fragment or raise error
        if curr_fragment_len + curr_text_len > max_len:
            # can not continue the fragment
            if not curr_fragment:
                raise ValueError(f"Message is too long to be split into fragments of length {max_len}")
            
            # finish fragment
            yield ''.join(curr_fragment)

            # start new fragment
            curr_fragment = []
            curr_fragment_len  = 0
        
        curr_fragment.append(curr_text)
        curr_fragment_len += curr_text_len



def test():
    source = "<p>Hello, <b>world</b>!</p>"
    max_len = 10
    res = split_message(source, max_len)
    for _ in res:
        print(_)

if __name__ == "__main__":
    test()

    