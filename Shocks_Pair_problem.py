# a = list(map(int, input("enter some numbers with spacing: ").split()))
#print(a)

#Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. 
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.

import math
import os
import random
import re
import sys

n = int(input("please enter the numbers of number: "))
ar = list(map(int, input("please enter the elements: ").rstrip().split()))


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    li = [ ]
    b = 0
    for num in ar:
        if num not in li:
            li.append(num)
    z = len(li)
    
    # for i in range(0, z):
    #     a = ar.count(li[i])
    #     c = a // 2
    #     if c >= 0:
    #         b = b + c
    # return b
    
    for i in range(0, z):
        x = li[i]
        count = 0
        for ele in ar: 
            if (ele == x): 
                count = count + 1
        c = count // 2
        if c >= 0:
            b = b + c
        else:
            break

    return b

result = sockMerchant(n, ar)
print(result)

