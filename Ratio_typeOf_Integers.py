#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    cnt_negative = 0
    cnt_positive = 0
    cnt_zero = 0
    for num in arr:
        if num < 0:
            cnt_negative = cnt_negative + 1
        elif num > 0:
            cnt_positive = cnt_positive + 1
        else:
            cnt_zero = cnt_zero + 1

    A = round(cnt_positive/n, 4)
    B = round(cnt_negative/n, 4)
    C = round(cnt_zero/n, 4)
    print(A)
    print(B)
    print(C)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
