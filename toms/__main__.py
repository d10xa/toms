import sys
from typing import Iterator

from toms import convert_toms_str


def flat_stdin() -> Iterator[str]:
    import itertools
    return itertools.chain.from_iterable((i.split() for i in sys.stdin))


def main():
    args = (sys.argv[1:] or flat_stdin())
    for x in (convert_toms_str(r) for r in args):
        print(x)


if __name__ == '__main__':
    main()
