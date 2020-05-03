# The concept of slicing in Python
# Star, Stop, Step

# STAR and STOP slicing
name = 'Lebron James'

print(name[0:4])  # Lebr - prints our from the element at 0 not including the element at 4 (RULE: Up to but not
# including).
print(name[2:9])  # bron Ja
# in slicing you can also use negative integers and you can using two elements is not required. With negative
# indexing you can't go backwards. It should also be noted that in slicing, when using a negative integer,
# the rule "UP TO BUT NOT" is backwards
print(name[:10])  # Lebron Jam
print(name[-10:])  # bron James
print(name[5:])  # n James
print()
# Mini Exercise
# Find many ways to slice the word blue from the variable parrot
parrot = 'Norwegian Blue'
print(parrot[10:14])  # Blue
print(parrot[10:])  # Blue
print(parrot[10 - 14:])  # Blue
print(parrot[-4:])
print()
print(parrot[:6] + parrot[6:])  # Norwegian Blue
# Letters slicing
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[-2:-4])  # there will be no output from this slicing because you can't go backwards
print(alphabet[-4:-2])  # wx
print(alphabet[:-2])  # abcdefghijklmnopqrstuvwx

# STEP slicing

print(parrot[:6:2])  # Nre
print(parrot[3:10:4])  # na

number2 = '120,223,372,036,854,775,807'
number = '9,223,372,036,854,775,807'
print(number2[1::3])
print()
print(number[1::4])
print()
# The difference between the two "equation" is that one tells you where to stop and the other one doesn't
# this is why step slicing is so helpful
num = '9,223;372:036 854,775;807'
seperators = num[1::4]
print(seperators)
print()
values = "".join(char if char not in seperators else " " for char in num).split()
print([int(val) for val in values])

# slicing backwards with negative integers * always make sure that the start value is greater then the stop value
backwards = alphabet[25::-1] # zyxwvutsrqponmlkjihgfedcba
print(backwards)
forward = alphabet[24:26:-1] # this will not work because the start int is lesser then the stop int and the step
# can't go backwards '-1'
print(forward)
