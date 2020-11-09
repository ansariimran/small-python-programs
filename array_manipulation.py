import math
import os
import random
import re
import sys






# arr = list(map(str, input().split()))
arr = list(input().split())
new_arr = arr[: : -1]
    
for i in new_arr:
    print(i, end=" ")

#method-2
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    l = len(arr)
    new_arr = arr[: : -1]
    print(' '.join(map(str, new_arr)))