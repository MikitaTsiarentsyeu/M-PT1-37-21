#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from time import sleep


def print_warning(warning_str, delay=1.5):
    """ Вывод предупреждения с задержкой на указанное время (сек.) и с возвратом каретки в начало строки.
    """
    print(f'\r{warning_str}', end='')
    sleep(delay)
    print('\r', end='')


def calc_qe():
    # первоначальные значения коэффициентов
    coeff_dict = dict.fromkeys(('a', 'b', 'c'), 0)
    # вывод заголовка
    title = 'Расчёт квадратного уравнения по формуле: a*x**2-b*x-c=0'
    print('-' * len(title), title, '-' * len(title), sep='\n')
    # пользовательский интерфейс (запрос и изменение коэффициентов)
    for i in coeff_dict:
        while True:
            try:
                # запрос ввода значения коэффициента и проверка введённой строки
                coeff_dict[i] = int(input(f'Введите коэф."{i}": '))
                if coeff_dict[i]:
                    break
                print_warning('Необходимо указать ненулевое число!')
            except ValueError:
                print_warning('Необходимо указать ненулевое целое число!')
    title = 'Результирующая формула: %s*x**2%s%s*x%s%s=0' % (coeff_dict['a'],
                                                             '+' if coeff_dict['b'] < 0 else '-',
                                                             coeff_dict['b'] * (-1 if coeff_dict['b'] < 0 else 1),
                                                             '+' if coeff_dict['c'] < 0 else '-',
                                                             coeff_dict['c'] * (-1 if coeff_dict['c'] < 0 else 1))
    print('-' * len(title), title, '-' * len(title), sep='\n')
    # расчёт и вывод результата
    d = (-1 * coeff_dict['b']) ** 2 + 4 * coeff_dict['a'] * coeff_dict['c']
    print('Уравнение не имеет решений.' if d < 0 else
          f'x{"" if d == 0 else "1"} = {((coeff_dict["b"]) - math.sqrt(d)) / (2 * coeff_dict["a"])}')
    if d > 0:
        print(f'x2 = {((coeff_dict["b"]) + math.sqrt(d)) / (2 * coeff_dict["a"])}')


if __name__ == '__main__':
    calc_qe()
