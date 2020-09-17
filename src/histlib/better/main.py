import argparse
from dataclasses import dataclass

from histlib.better import hist as hbh


@dataclass
class MinMaxKeyCounter:
    min_key: str
    max_key: str
    min_counter: int
    max_counter: int

    def __str__(self) -> str:
        s = f'Min Key = {self.min_key} with count = {self.min_counter}\n'
        s += f'Max Key = {self.max_key} with count = {self.max_counter}'
        return s


def do_it(fname: str) -> MinMaxKeyCounter:
    with open(fname) as f:
        hist = hbh.find_hist(f)
        min_kv = hbh.min_key_value(hist)
        max_kv = hbh.max_key_value(hist)

    return MinMaxKeyCounter(
        min_key=min_kv.key,
        max_key=max_kv.key,
        max_counter=max_kv.value,
        min_counter=min_kv.value
    )


def main():
    parser = argparse.ArgumentParser(
        description='compute the entry with the most occurence and the least occurence form a file')
    parser.add_argument('fname', metavar='N', type=str,
                        help='compute the')
    args = parser.parse_args()

    mmkc = do_it(args.fname)

    print(mmkc)


if __name__ == '__main__':
    main()
