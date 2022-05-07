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
print(num1, num2)
score = 0
while True:
    sign = input('Choice: ')
    if sign == "+":
        correct_answer = num1 + num2
        break
    elif sign == "-":
        correct_answer = num1 - num2
        break
    elif sign == '*':
        correct_answer = num1 * num2
        break
    else:
        print('Try again!')
        continue

def get_guess():
    user_answer = int(input(str(num1) + ' ' + sign + ' ' + str(num2) + " = "))
    return user_answer 
tries = 0
for i in range(10):
    for i in range(3):
        user_answer = get_guess()
        if user_answer == correct_answer:
            print('Correct!')
            break
        else:
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
    random_nums()