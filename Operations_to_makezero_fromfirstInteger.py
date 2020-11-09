n = int(input("Enter a number to perform action on: "))

def Operations_to_makezero_fromfirstInteger(N):
    count = 0
    cond = True

    if N <= 1000000000 and N >=1:
        while cond:
            first = str(N)
            first_digit = int(first[0])

            if N == 0:
                cond = False
            else:
                N = N - first_digit
                count = count + 1
        return count

    

ans = Operations_to_makezero_fromfirstInteger(n)
print(ans)