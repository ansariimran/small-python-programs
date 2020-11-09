# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

while T:
    myString = input()
    n = len(myString)

    string1 = myString[0 : n : 2]
    string2 = myString[1 : n : 2]

    print(f"{string1} {string2}")

    T = T-1