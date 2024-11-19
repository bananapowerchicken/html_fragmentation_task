from types import Generator


MAX_LEN = 4096


def split_message(source: str, max_len=MAX_LEN) -> Generator[str]:
    """
    Splits the original message (`source`) into fragments of the specified
    length (`max_len`)
    """