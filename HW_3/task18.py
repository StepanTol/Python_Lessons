'''Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X'''

'''from random import randint

N = int(input("Введите количество элементов списка: "))

lst = []
for i in range(N):
    lst.append(randint(-5, 5)) #Строки 11 - 12 - 13 можно записать как: lst = [randint(a, b) for i in range(N)]
print(lst)

X = int(input("Введите число: "))
index = 0
min = abs(X - lst[0])
for i in range(len(lst)):
    value = abs(X - lst[i])
    if value < min:
        min = value
        index = i # b = [abs(lst[i] - X) for i in range(len(lst))] - создаём второй массив
print(lst[index])''' # lst[b.index(min(b))] - берём индекс мин-го элемента из второго массива и находим этот же индекс в первом массиве

# Решение через словарь

from random import randint

n = int(input('n = '))
lst = [randint(1, n) for _ in range(n)]

print(lst)

x = int(input('x = '))

dct = {abs(x - item):item for item in lst} # Генератор словаря

print(dct)
print(dct[min(dct)])