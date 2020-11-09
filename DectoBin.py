num = int(input("Enter any number: "))

def DecimalToBinary(num):
        if num > 1:
            DecimalToBinary(num // 2)
        a = (num % 2)
        print(type(a))

DecimalToBinary(num)