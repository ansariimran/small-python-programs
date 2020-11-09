N = int(input("pllk: "))


def LastDigit(N):
    if N >= 1 and N <= 10000:
        a = str(N)
        l = len(a)
        b = int(a[l-1])
        print(b)


LastDigit(N)