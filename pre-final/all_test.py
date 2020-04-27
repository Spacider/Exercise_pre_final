#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

from itertools import combinations

def number_of_words_in_dictionary(word_1, word_2):
    with open('dictionary.txt') as file:
        all_file = file.readlines()

    all_file = [_.strip() for _ in all_file]
    if word_1 not in all_file and word_2 not in all_file:
        if word_1 == word_2:
            print(f'Could not find {word_1} in dictionary.')
        else:
            print(f'Could not find at least one of {word_1} and {word_2} in dictionary.')
    else:
        if word_1 not in all_file:
            print(f'{word_2} is in dictionary.')
        elif word_2 not in all_file:
            print(f'{word_1} is in dictionary.')
        else:
            word_1_index = all_file.index(word_1)
            word_2_index = all_file.index(word_2)
            print(f'Found {abs(word_2_index - word_1_index) + 1} words between {word_1} and {word_2} in dictionary')





if __name__ == '__main__':
    number_of_words_in_dictionary('COMPANY', 'comparison')


