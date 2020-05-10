# import the module random to generate a random number between 1-10
import random

random_answer = random.randint(1, 10)

answer = None
print("--------Welcome to the Guessing game----------")
while random_answer != answer:
    answer = int(input("Enter a number between 1-10: "))
    if answer == random_answer:
        print('You guess the right number')
        break
    elif answer > random_answer:
        print('You guessed the wrong number. Try again and guess lower')
    else:
        print('You guessed the wrong number. Try again and guess higher')
