N = int(input("pleaseygvu : "))

def AllPair(N):
    flag = True
    x = 1
    count = 0
    while flag:
        if x == N:
            flag = False
            return count
        else:
            count = count+1
            x = x+1
    
print(AllPair(N))