#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

def rectangle(width, height):
    '''
    ab
    dc
    ef
    '''
    result_list = []
    a_aksii = ord('a') - 1
    for i in range(height):
        single_str = ''
        for j in range(width):
            a_aksii = a_aksii + 1
            if a_aksii > ord('z'):
                a_aksii = ord('a')
            print(a_aksii)
            single_str = single_str + chr(a_aksii)
        result_list.append(single_str)
    print(result_list)
    # ['ab', 'cd', 'ef']
    for index in range(len(result_list)):
        if index % 2 == 0:
            print(result_list[index])
        else:
            print(result_list[index][::-1])





if __name__ == '__main__':
    print(rectangle(17, 4))


