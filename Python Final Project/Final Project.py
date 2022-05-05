import random
def random_nums():
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    return num1, num2

print( """
Enter the sign for the problem type desired.
    + Addition
    - Subtraction
    * Multiplication
""" )
sign = input('Choice: ')
sign = sign.lower()
sign = sign.strip()
print(sign)