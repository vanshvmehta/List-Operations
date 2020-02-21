"""
To search for an element in a list using binary search
"""

from random import randint


def binary(n):
    k = int(input('Enter the integer to be searched: '))
    lw, hi = 0, n - 1
    while hi >= lw:
        mid = (hi + lw) // 2
        if l[mid] > k:
            hi = mid
        elif l[mid] < k:
            lw = mid + 1
        elif l[mid] == k:
            print('Integer found in the position', mid)
            break
    else:
        print('Integer not found in the list')
    

while True:
    l = [randint(1000, 9999) for i in range(10)]
    print('List: ', l)
    binary(10)
    print('-' * 50)
