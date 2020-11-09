n = int(input("please enter the numbers of number: "))
ar = list(map(int, input("please enter the elements: ").rstrip().split()))


# Complete the sockMerchant function below.
def max_number_occurances(n, ar):
    the_number = 0
    for num in ar:
        if num > the_number:
            the_number = num
    print(f"the maximum number in the list is {the_number}")
    
    count = 0
    for num in ar:
        if num == the_number:
            count = count + 1
    return count    

result = max_number_occurances(n, ar)
print(f"the maximum number comes {result} times in the list")