arr = list(map(int, input().rstrip().split()))

def miniMaxSum(arr):
    n = 5
    minsum = 0
    maxsum = 0
    arr.sort()
    for i in range(1, n):
        maxsum = maxsum + arr[i]
    for i in range(0, n-1):
        minsum = minsum + arr[i]
    print(f"{minsum} {maxsum}")

miniMaxSum(arr)