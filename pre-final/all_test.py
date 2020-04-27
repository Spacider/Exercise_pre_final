#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

from itertools import combinations

def subnumbers_whose_digits_add_up_to(number, sum_of_digits):
    result = set()
    list_a = list(map(int, str(number)))

    lens = 1
    while lens <= len(list_a):
        for item in list(combinations(list_a, lens)):
            print(item)
            if sum(item) == sum_of_digits:
                result.add(int("".join(map(str, item))))
        lens += 1

    return [_ for _ in result]


if __name__ == '__main__':
    print(subnumbers_whose_digits_add_up_to(123, 6))


