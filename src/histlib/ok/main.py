import argparse
from dataclasses import dataclass


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
    counter = {}
    max_key = None
    max_counter = 0
    min_key = None
    min_counter = 0

    # fill up histogram
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip()
            if line in counter:
                counter[line] += 1
            else:
                counter[line] = 1

    # find max key
    for k, v in counter.items():
        if max_key is None or v > max_counter:
            max_key = k
            max_counter = v
        if min_key is None or v < min_counter:
            min_key = k
            min_counter = v

    return MinMaxKeyCounter(
        min_key=min_key,
        max_key=max_key,
        max_counter=max_counter,
        min_counter=min_counter
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
