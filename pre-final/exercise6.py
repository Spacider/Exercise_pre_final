#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

# ord(c) returns the encoding of character c. # chr(e) returns the character encoded by e.
def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    result_list = []
    a_aksii = ord('a') - 1
    for i in range(height):
        single_str = ''
        for j in range(width):
            a_aksii = a_aksii + 1
            if a_aksii > ord('z'):
                a_aksii = ord('a')
            single_str = single_str + chr(a_aksii)
        result_list.append(single_str)
    # ['ab', 'cd', 'ef']
    for index in range(len(result_list)):
        if index % 2 == 0:
            print(result_list[index])
        else:
            print(result_list[index][::-1])