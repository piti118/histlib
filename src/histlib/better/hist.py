from dataclasses import dataclass
from typing import Iterable, Dict


@dataclass
class KeyValue:
    key: str
    value: int


def find_hist(data: Iterable[str]) -> Dict[str, int]:
    counter = dict()
    for d in data:
        d = d.strip()
        if d in counter:
            counter[d] += 1
        else:
            counter[d] = 1
    return counter


def max_key_value(d: Dict[str, int]) -> KeyValue:
    max_key = None
    max_value = None
    if len(d) == 0:
        raise ValueError('Dict is Empty')
    for k, v in d.items():
        if max_key is None or v > max_value:
            max_key = k
            max_value = v
    return KeyValue(max_key, max_value)


def min_key_value(d: Dict[str, int]) -> KeyValue:
    min_key = None
    min_value = None
    if len(d) == 0:
        raise ValueError('Dict is Empty')
    for k, v in d.items():
        if min_key is None or v < min_value:
            min_key = k
            min_value = v
    return KeyValue(min_key, min_value)
