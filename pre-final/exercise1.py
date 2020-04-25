#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'



def rearrange(number):
    '''
    Returns an integer consisting of all nonzero digits in "number", from smallest to largest.
    You can assume that "number" is a valid strictly positive integer.
    >>> rearrange(1)
    1
    >>> rearrange(200)
    2
    >>> rearrange(395)
    359
    >>> rearrange(10029001)
    1129
    >>> rearrange(301302004)
    12334
    >>> rearrange(9409898038908908934890)
    33448888889999999
    '''
    list_a = [item for item in str(number)]
    result_list = [item for item in list_a if item != '0']
    str1 = ''
    for item in sorted(result_list):
        str1 += item
    return int(str1)

if __name__ == '__main__':
    rearrange(200)