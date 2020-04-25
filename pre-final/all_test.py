#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

import string

def words(text):
    punctuation_string = string.punctuation
    for item in punctuation_string:
        text = text.replace(item, '')
    split_text = text.split(' ')
    ['Twelve', 'will,', 'believe', 'me,', 'be', 'quite', 'enough', 'for', 'your', 'purpose.']
    result_list = [set() for _ in range(len(split_text))]
    for item in split_text:
        result_list[len(item)].add(item.lower())
    for item in result_list:
        if item != []:
            print(f'Words of length {result_list.index(item)}:')
            print('    ', end= '')
            print(sorted(item))

if __name__ == '__main__':
    print(words('Twelve will, believe me, be quite enough for your purpose.'))