#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of nothing but lowercase letters.
    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aabbccddee')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwijlrstuvabcde')
    'rstuv'
    '''
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