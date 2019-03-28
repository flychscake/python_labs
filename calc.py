#!/usr/bin/env python
# -*- coding: utf-8 -*-
print('Разделитель - /')

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def add(n, m):
    if n[1] == m[1]:
        print('{}/{}'.format(n[0]+m[0], n[1]))
    else:
        cd = int(n[1]*m[1]/gcd(n[1], m[1]))
        rn = int(cd/n[1]*n[0]+cd/m[1]*m[0])
        g2 = gcd(rn, cd)
        n = int(rn/g2)
        d = int(cd/g2)
        print('{}/{}'.format(n, d) if n != d else n)

def diff(n, m):
    if n[1] == m[1]:
        print('{}/{}'.format(n[0]-m[0], n[1]))
    else:
        cd = int(n[1]*m[1]/gcd(n[1], m[1]))
        rn = int(cd/n[1]*n[0]-cd/m[1]*m[0])
        g2 = gcd(rn, cd)
        n = int(rn/g2)
        d = int(cd/g2)
        print('{}/{}'.format(n, d) if n != d else n)

def divide(n, m):
    g1 = n[0] * m[1]
    g2 = n[1] * m[0]
    gd = gcd(g1, g2)
    g1 = int(g1/gd)
    g2 = int(g2/gd)
    print('{}/{}'.format(g1, g2))

def multiply(n, m):
    g1 = n[0] * m[0]
    g2 = n[1] * m[1]
    gd = gcd(g1, g2)
    g1 = int(g1/gd)
    g2 = int(g2/gd)
    print('{}/{}'.format(g1, g2))

while True:
    x, y = 0, 0
    try:
        x = [int(z) for z in input('Введите первую дробь: ').split('/')]
        y = [int(z) for z in input('Введите вторую дробь: ').split('/')]
    except:
        print('Неверный ввод')
        continue
    if not (1 < len(x) < 3) or not (1 < len(y) < 3):
        print('Неверный ввод')
        continue
    action_correct = False
    while not action_correct:
        action = input('Выберите действие + - / * :')
        if action not in ('+', '-', '/', '*'):
            print('Неверное действие')
            continue
        action_correct = True
        if action == '+':
            add(x, y)
        elif action == '-':
            diff(x, y)
        elif action == '/':
            divide(x, y)
        elif action == '*':
            multiply(x, y)



