import sys
from toms import convert_toms_str


def main():
    args = sys.argv[1:]
    for arg in args:
        print(convert_toms_str(arg))


if __name__ == '__main__':
    main()
