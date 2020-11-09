n = int(input("please enter the number of steps: "))

for i in range(n):
    A = (n-1-i) * " "
    B = (i+1) * "#"
    print(f"{A}{B}")
    # print(f"{B}{A}")