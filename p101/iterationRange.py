# prints a value from 10 and up to but not including 16
for i in range(10, 16):
    print("i is now {}".format(i))
print()
# you can write a program without a start value
for i in range(10):
    print("i is now {}".format(i))
print()
# you can also use the slicing step philosophy in a range loop
# print out all even numbers
for i in range(0, 10, 2):
    print(i)
    print()
# you can do the same going backwards using a negative int as a step
# print out all the multiples of 3 using starting at 21
for i in range(21, 0, -3):
    print(i)
print()
# this may not be a conventional way to use the in range loop but this could be of great exercise
age = int(input("How old are you"))
if age in range(15, 19):
    print("You are old enough to be in High School.")
else:
    print("Based on your age, you can't attend High School.")
    print()
# the above code is the same as doing this below
# if age >= 15 and age < 19:
#     print("You are old enough to be in High School.")
# else:
#     print("Based on your age, you can't attend High School.")
#     print()

# Write a program to print out all the numbers from 0 to 100 that are divisible by 7. Note that zero is considered to
# be divisible by all other integers, so your output should include zero.

for i in range(0, 100):
    if i % 7 == 0:
        print("{} is divisible by 7.".format(i))
print()
# Nested loops times table
for i in range(1, 11):
    for j in range(1, 11):
        print('{0} times {1} is {2}'.format(i, j, (i * j)))
    print('----------')
