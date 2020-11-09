#!/bin/python3

import math
import os
import random
import re
import sys



def diagonalDifference(arr):
    diagonal1 = 0
    diagonal2 = 0
    for i in range(n):
        diagonal1 = arr[i][i] + diagonal1
        diagonal2 = arr[i][n-1-i] + diagonal2

    if diagonal1 < diagonal2:
        answer = diagonal2 - diagonal1
    else:
        answer = diagonal1 - diagonal2

    return answer


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(f"diagonal Difference of the array is {diagonalDifference(arr)}")

    # result = diagonalDifference(arr)
    # fptr.write(str(result) + '\n')
    # fptr.close()
