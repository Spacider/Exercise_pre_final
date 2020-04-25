#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

def longest_leftmost_sequence_of_consecutive_letters(word):
    str = ''
    max_len_str = ''

    for index in range(len(word)):
        str = word[index]
        str = find_longest_len(index, word, str)
        if len(str) > len(max_len_str):
            max_len_str = str

    return max_len_str

def find_longest_len(index, word, str):
    if index + 1 < len(word):
        if ord(word[index]) == ord(word[index + 1]) - 1:
            str = str + word[index + 1]
            str = find_longest_len(index + 1, word, str)
    return str

if __name__ == '__main__':
    print(longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt'))


