try:
    number_of_elements = int(input())
    emptyList = {}
    while number_of_elements:
        a = list(input().split())
        key = a[0]
        value = int(a[1])
        emptyList[key] = value
        a.clear()
        number_of_elements = number_of_elements-1



    count = 0
    keys = [ ]
    flag = True
    while flag:
        test = input()
        keys.append(test)
        if test == "":
            flag = False
    l = len(keys)
    keys.remove(keys[l-1])
    for key in keys:
        if key in emptyList:
            print(f"{key}={emptyList[key]}")
        elif key not in emptyList:
            print("Not found")

except:
    pass


# print(emptyList)