import sys
from typing import Iterator

from toms import convert_toms_str


def flat_stdin() -> Iterator[str]:
    import itertools
    return itertools.chain.from_iterable([i.split() for i in sys.stdin])


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        args = list(flat_stdin())
    for arg in args:
        print(convert_toms_str(arg))


if __name__ == '__main__':
    main()
