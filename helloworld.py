
'''
print(int(input("gimme ur number bitch: "))*2)
'''
num = input("Please input a number: ")
try:
    num=float(num)
    print(num*2)
except ValueError:
    print("Invalid Input. Please type a valid number.")
