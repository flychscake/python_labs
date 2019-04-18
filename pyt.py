
# -*- coding: utf-8 -*-

from datetime import date
from random import randint
def task7_1():
    n = [int(x) for x in input('Введите числа через пробел: ').split()]
    do_exists = False
    for x in n:
        if x%3==0:
            do_exists = True
    print('Есть') if do_exists==True else print('Нет')

def task7_2():
    n, m = [int(x) for x in input('Введите количество чисел и число (0-4) для поиска: ').split()]
    num_array = [str(randint(0, 4)) for x in range(0, n)]
    get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
    print('{num_array}\nИндексы числа {m} - {m_indexs}'.format(num_array=num_array, m=m, m_indexs=get_indexes(str(m), num_array)))

def task7_3():
    n = int(input('Введите количество чисел:'))
    num_array = [randint(0, 100) for x in range(0, n)]
    print('{arr}\nМинимальный № - {index_min}\nМаксимальный № - {index_max}'.format(arr=num_array, index_min=num_array.index(min(num_array)), index_max=num_array.index(max(num_array))))

def task7_4():
    n = int(input('Введите количество чисел:'))
    num_array = [randint(0, 100) for x in range(0, n)]
    print('{orig}\n{sorted}'.format(orig=num_array, sorted=sorted(num_array)))

def task7_5():
    n = int(input('Введите количество чисел:'))
    num_array = [randint(0, 100) for x in range(0, n)]
    print(num_array)
    num_array.sort(key=lambda line: int(str(line)[0]))
    print(num_array)

def task7_6():
    get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
    n = int(input('Введите количество чисел: '))
    num_array = [randint(0, 100) for x in range(0, n)]
    num_sorted = sorted(num_array)
    index_array = []
    for x in num_sorted:
        index_array.append(num_array.index(x))
    print('{0}\n{1}\nIndexes - {2}'.format(num_array, num_sorted, index_array))

def task7_7():
    def sorting(mas):
        for i in range(n-1):
            for j in range(n-2, i-1 ,-1):
                if mas[j+1] < mas[j]:
                    mas[j], mas[j+1] = mas[j+1], mas[j]
        return mas

    n = int(input('Введите количество чисел: '))
    num_array = [randint(0, 100) for x in range(0, n)]
    print(num_array)
    sorted_array = sorting(num_array)
    print(num_array)
    count_elements = {}
    for x in sorted_array:
        count_elements[str(x)]=[y for y in sorted_array if y==x]
        count_elements[str(x)]=len(count_elements[str(x)])
    
    print(count_elements)
        
def task7_8():
    def sorting(mas):
        for i in range(n-1):
            for j in range(n-2, i-1 ,-1):
                if mas[j+1] < mas[j]:
                    mas[j], mas[j+1] = mas[j+1], mas[j]
        return mas

    n = int(input('Введите количество чисел: '))
    num_array = [randint(0, 100) for x in range(0, n)]
    print(num_array)
    sorted_array = sorting(num_array)
    print(num_array)
    count_elements = {}
    ifself_elements = {}
    for x in sorted_array:
        count_elements[str(x)]=[y for y in sorted_array if y==x]
        ifself_elements[str(x)]=len(count_elements[str(x)])
    
    length_series = []
    series = []
    for k, v in count_elements.items():
        series.append(v)
        length_series.append(len(v))
    print(length_series)
    print(series)

task7_8()