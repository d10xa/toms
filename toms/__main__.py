import itertools
import sys
from typing import Iterator

from toms import convert_toms_str
from toms import replace_millis_str


def flat_stdin() -> Iterator[str]:
    return itertools.chain.from_iterable((i.split() for i in sys.stdin))


def main():
    if sys.argv[1] == "now":
        import time
        millis = int(round(time.time() * 1000))
        print(millis)
    elif sys.argv[1] == "replace":
        for x in sys.stdin:
            sys.stdout.write(replace_millis_str(x))
    else:
        args = (iter(sys.argv[1:]) or flat_stdin())
        for x in (convert_toms_str(r) for r in args):
            print(x)


if __name__ == '__main__':
    main()
