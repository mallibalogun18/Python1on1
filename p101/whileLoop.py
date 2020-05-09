# for loop example
print("For loop code")
for i in range(10):
    print('i is now {}.'.format(i))
print('-------------------------')
print()
# while loop example
print("While loop code")
upper = 0
while upper < 10:
    print('The number is {}.'.format(upper))
    upper += 1
print()
# elevator program using while loop
print('-------------------------')
print("""\t\t\t\tThe Elevator Game""")
elevator_floor = [1,2,3,4,5,6]
floor = ''
answer = ''
while floor not in elevator_floor:
    floor = int(input("Please select the floor you would like to exit from"))
    if floor == 0:
        answer = int(input('If you want to quit the game press 0 again.'))
        if answer == 0:
            break

if answer == 0:
    print("""Sorry but you've quit the game. Good bye.""")
else:
    print("You select the floor on level {}. Door's are open. You may exit.".format(floor))

# Write a program to print out all the numbers from 0 to 20 that aren't divisible by 3 or 5
print()
for i in range(21):
    if i%3==0 or i%5==0:
        continue
    print(i)
