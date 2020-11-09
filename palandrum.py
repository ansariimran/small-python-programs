input = input("please type a word to check if palandrum or not :  ")

def palandrum(num):
    check = num[: : -1]

    if check == num:
        print("its a palandrum")
    else:
        print("not a palandrum")

palandrum(input)