import math

n = int(input("Enter the number to make it a perfect square: "))
number = 2

def perfect_square(n):
    count1 = 0
    x = n
    cond1 = True
    
    while cond1:
        sqrut1 = math.sqrt(x)
        if (sqrut1 - math.floor(sqrut1)) == 0:
            cond1 = False
        else:
            x = x + number
            count1 = count1 + 1
    
    count2 = 0
    y = n
    cond2 = True
    while cond2:
        sqrut2 = math.sqrt(y)
        if (sqrut2 - math.floor(sqrut2)) == 0:
            cond2 = False
        else:
            y = y - number
            count2 = count2 + 1

    if count2 > count1:
        return count1
    else:
        return count2

ans = perfect_square(n)
p_square = n - number*ans # Modify for each case

# z = n * number**ans #in case of mulplication, do power & in case of addition, do multiply
print("perfect square near the given number: " + str(p_square))
print("Qube root of perfect square: " + str(math.sqrt(p_square)))

print(f"Minimum Operation taken to make a perfect square is {ans} ")