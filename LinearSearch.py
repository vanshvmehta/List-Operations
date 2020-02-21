"""
To find an element in a randomly generated list of 10 numbers using linear search
"""

from random import randint


def linear():
    k = int(input('Enter the integer to be search: '))
    for i in range(10):
        if l[i] == k:
            print('Value found at position ', i)
            break
    else:
        print('Value not found')


while True:
    l = [randint(1000, 9999) for i in range(10)]
    print('List: ', l)
    linear()
    print('-' * 50)
