#!/usr/bin/env python
# -*- coding: utf-8 -*-

get_sum_nested_list_v1 = lambda int_list: sum(get_sum_nested_list_v1(i) if isinstance(i, list) else i for i in int_list)

get_sum_nested_list_v2 = lambda item, result=0: result + sum(map(get_sum_nested_list_v2, item)) if type(
    item) == list else item

if __name__ == '__main__':
    title = 'Проверка рекурсивных функций вычисления суммы всех элементов (чисел) вложенного списка'
    print('-' * len(title), title, '-' * len(title), sep='\n')
    int_list = [1, 2, [2, 4, [[7, 8], 4, 6]]]
    print('int_list =', int_list)
    print('result v1 =', get_sum_nested_list_v1(int_list))
    print('result v2 =', get_sum_nested_list_v2(int_list))
