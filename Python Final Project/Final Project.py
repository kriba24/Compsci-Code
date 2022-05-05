"""
Math Tutor
"""
import random
tries = 0
sign = ""
user_answer = 0
num1 = 0
num2 = 0
def gen_nums():
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    return num1, num2
input_block = """
Enter the number for the problem type desired.
    1. Addition
    2. Subtraction
    3. Multiplication
"""
print(input_block)
choice = input('Enter choice: ')
gen_nums()
if choice == 1:
    sign = " + "
    correct_answer = num1 + num2
elif choice == 2:
    sign = " - "
    correct_answer = num1 - num2
elif choice == 3:
    sign = " * "
    correct_answer = num1 * num2
def get_answer():
    user_answer = int(input(str(num1) + str(sign) + str(num2) + " = "))
    return user_answer
