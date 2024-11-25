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

    