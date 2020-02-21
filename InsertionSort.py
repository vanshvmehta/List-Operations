"""
To sort a list using insertion sort
"""

from random import randint


def insertion(n):
    for i in range(1, n):
        temp, j = l[i], i - 1
        while j >= 0 and l[j] > temp:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = temp
    print(l)
    

while True:
    l = [randint(1000, 9999) for i in range(10)]
    print('List: ', l)
    insertion(10)
    print('-' * 50)
    input('Press Enter to do the same for another list')
