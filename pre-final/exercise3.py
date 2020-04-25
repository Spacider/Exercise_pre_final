#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

import math

def single_factors(number):
    '''
    Returns the product of the prime divisors of "number" (using each prime divisor only once).
    You can assume that "number" is an integer at least equal to 2.
    >>> single_factors(2)
    2
    >>> single_factors(4096)
    2
    >>> single_factors(85)
    85
    >>> single_factors(10440125)
    85
    >>> single_factors(154)
    154
    >>> single_factors(52399401037149926144)
    154
    '''
    # 方法1: 用集合（不重复）
    k = 2
    all_possible_number = set()
    while number != 1:
        if number % k == 0:
            all_possible_number.add(k)
            number = number // k
        else:
            k += 1
    sum = 1
    for i in all_possible_number:
        sum *= i

    return sum
    # 方法2: 穷举
    # product = 1
    #
    # if (number % 2 == 0):
    #     product *= 2
    #     while number % 2 == 0:
    #         number = number // 2
    #
    #
    # for i in range(3, int(math.sqrt(number)), 2):
    #     if number == 1:
    #         break
    #     if (number % i == 0):
    #         product = product * i
    #         while (number % i == 0):
    #             number = number // i
    #
    # if (number > 2):
    #     product = product * number
    #
    # return int(product)