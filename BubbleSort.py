"""
To sort a list using bubble sort
"""

from random import randint


def bubble():
    i = 0
    while i < 10:
        for j in range(0, 10 - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
        i += 1
    print('Sorted List: ', l)


while True:
    l = [randint(1000, 9999) for i in range(10)]
    print('List: ', l)
    bubble()
    print('-' * 50)
    input('Press Enter to do the same for another list')
