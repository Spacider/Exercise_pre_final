#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

def rearrange(L, from_first = True):
    '''
    Returns a new list consisting of:
    * in
    * in
    case "from_first" is True:
    L’s first member if it exists, then
    L’s last member if it exists, then
    L’s second member if it exists, then
    L’s second last member if it exists, then L’s third member if it exists...
    case "from_first" is False:
    L’s last member if it exists, then
    L’s first member if it exists, then
    L’s second last member if it exists, then L’s second member if it exists, then
    L’s third last member if it exists...
    >>> L = []
    >>> rearrange(L), L
    ([], [])
    >>> L = [10]
    >>> rearrange(L, False), L
    ([10], [10])
    >>> L = [10, 20]
    >>> rearrange(L), L
    ([10, 20], [10, 20])
    >>> L = [10, 20, 30]
    >>> rearrange(L), L
    ([10, 30, 20], [10, 20, 30])
    >>> L = [10, 20, 30, 40]
    >>> rearrange(L, False), L
    ([40, 10, 30, 20], [10, 20, 30, 40])
    >>> L = [10, 20, 30, 40, 50]
    >>> rearrange(L, False), L
    ([50, 10, 40, 20, 30], [10, 20, 30, 40, 50])
    >>> L = [10, 20, 30, 40, 50, 60]
    >>> rearrange(L), L
    ([10, 60, 20, 50, 30, 40], [10, 20, 30, 40, 50, 60])
    >>> L = [10, 20, 30, 40, 50, 60, 70]
    >>> rearrange(L), L
    ([10, 70, 20, 60, 30, 50, 40], [10, 20, 30, 40, 50, 60, 70])
    '''
    result_list = []
    L_length = len(L)
    if L_length <= 1:
        return L
    else:
        left = 0
        right = L_length - 1
        while len(result_list) < L_length:
            if from_first:
                if left == right:
                    result_list.append(L[left])
                else:
                    result_list.append(L[left])
                    result_list.append(L[right])
                left += 1
                right -= 1
            else:
                if left == right:
                    result_list.append(L[left])
                else:
                    result_list.append(L[right])
                    result_list.append(L[left])
                left += 1
                right -= 1
    return result_list
