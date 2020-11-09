
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    n = len(a)
    count1 = 0
    count2 = 0

    for i in range(n):
        if a[i] > b[i]:
            count1 = count1 + 1
        elif a[i] < b[i]:
            count2 = count2+1
    
    # return count1, count2
            
    print(f"{count1} {count2}")


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    
    compareTriplets(a, b)
    
    
    # result = compareTriplets(a, b)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
