"""
To reverse a randomly generated list
"""

from random import randint


def reverse():
    r = []
    for i in range(10 - 1, -1, -1):
        r += [l[i]]
    print('Reversed list is ', r)


while True:
    l = [randint(1000, 9999) for i in range(10)]
    print('List: ', l)
    reverse()
    print('-' * 50)
    input('Press Enter to do the same for another list')
