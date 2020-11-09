def pattern(n):
    # for i in range(1, n+1): 
    #     # print i number of * s in  
    #     # each line 
    #     print("*" * i)
    
    for i in range(1, n+1):
        li = [ ]
        # print("INCREMENTED FOR LOOP") 
        for j in range(1, i+1): 
            li.append(j)

        #print("\n DECREMENTED FOR LOOP") 
        for j in range(i-1, 0, -1): 
            li.append(j)
        # for num in li:
        #     print(num, end=" ") - This is used for printing all elements of all loop like: 1 1 2 1 1 2 3 2 1 (for n=3)
        print(" ".join(map(str, li)))
        li.clear()

    for i in range(n-1, 0, -1):
        li = [ ]
        # print("INCREMENTED FOR LOOP") 
        for j in range(1, i+1): 
            li.append(j)

        #print("\n DECREMENTED FOR LOOP") 
        for j in range(i-1, 0, -1): 
            li.append(j)
        # for num in li:
        #     print(num, end=" ") - This is used for printing all elements of all loop like: 1 1 2 1 1 2 3 2 1 (for n=3)
        print(" ".join(map(str, li)))
        li.clear()

pattern(5)