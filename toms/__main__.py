import itertools
import sys
from typing import Iterator

from toms import convert_toms_str
from toms import replace_millis_str


def flat_stdin() -> Iterator[str]:
    return itertools.chain.from_iterable((i.split() for i in sys.stdin))


def main():
    first_arg = sys.argv[1] if 1 < len(sys.argv) else None
    if first_arg == "now":
        import time
        millis = int(round(time.time() * 1000))
        print(millis)
    elif first_arg == "replace":
        for x in sys.stdin:
            sys.stdout.write(replace_millis_str(x))
    else:
        args_list = sys.argv[1:]
        if len(args_list) == 0:
            input_iter = flat_stdin()
        else:
            input_iter = iter(args_list)
        for x in (convert_toms_str(r) for r in input_iter):
            print(x)


if __name__ == '__main__':
    main()
