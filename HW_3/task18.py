'''Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X'''

from random import randint

N = int(input("Введите количество элементов списка: "))

lst = []
for i in range(N):
    lst.append(randint(-5, 5))
print(lst)

X = int(input("Введите число: "))
index = 0
min = abs(X - lst[0])
for i in range(len(lst)):
    value = abs(X - lst[i])
    if value < min:
        min = value
        index = i
print(lst[index])