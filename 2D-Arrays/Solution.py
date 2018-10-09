#!/bin/python3

import math
import os
import random
import re
import sys


def summ(arr):
    m = []
    for line in range(len(arr[0]) - 2):
        for tab in range(len(arr) - 2):
            current_sum = arr[line][tab] + arr[line][tab + 1] + arr[line][tab + 2] + arr[line + 1][tab + 1] + \
                          arr[line + 2][tab] + arr[line + 2][tab + 1] + arr[line + 2][tab + 2]
            m.append(current_sum)
    return (max(m))


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(summ(arr))