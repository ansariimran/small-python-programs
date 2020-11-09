number = int(input("enter a number : "))

def factorial(n):
    if n == 0:
        return 1
    else:
        yield (n * factorial(n - 1))

print(factorial(number))