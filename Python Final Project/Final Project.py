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
num1, num2 = random_nums()
score = 0
def gen_correct_answer():
    if sign == "+":
        correct_answer = num1 + num2
    elif sign == "-":
        correct_answer = num1 - num2
    elif sign == '*':
        correct_answer = num1 * num2
    return correct_answer

def get_guess():
    user_answer = int(input(str(num1) + ' ' + sign + ' ' + str(num2) + " = "))
    return user_answer 

while True:
    sign = input('Choice: ')
    if sign == "+" or sign == "-" or sign == "*":
        correct_answer = gen_correct_answer()
        break
    else:
        print('Try again!')
        continue
tries = 0
for i in range(10):
    for i in range(3):
        user_answer = get_guess()
        if user_answer == correct_answer:
            print('Correct!')
            break
        else:
            if tries < 2:
                print('Wrong. Try again!')
            tries += 1
    if tries == 0:
        score += 10
    elif tries == 1:
        score += 5
    elif tries == 2:
        score += 2
    else:
        print('You missed 3 times. The correct answer was ' + str(correct_answer) + ".")
        tries = 0
    num1, num2 = random_nums()
    correct_answer = gen_correct_answer()
print('Your score: ' + str(score))