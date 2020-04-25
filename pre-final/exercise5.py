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
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwijlrstuvabcde') 'rstuv'
    '''
