# Sequences in python is defined as an order set of items. Python as 5 types of sequences; string, tuple, range,
# list, bytes & byte array

# Sequence string operators
string1 = 'Hi, '
string2 = 'My name is '
string3 = 'James Brown '
string4 = 'and I like to '
string5 = 'dance and drink.'

print(string1 + string2 + string3 + string4 + string5)

# unlike other programming languages, you can multiple a string to repeat itself
print('Hello ' * 5)

today = 'Sunday'
print('day' in today)  # True
print('Sun' in today)  # True
print('sun' in today)  # False
print('thur' in today)  # False
print('James' in 'Michael')  # False

# String replacement fields
age = 18
print('My age is '+ str(age)+' years old.')
# another way to implement the above statement by using .format()
print('My age is {0} years old.'.format(age))
print('There {0} members in my family. I am {1}, my sisters are {2} and {3}, and my little brother is {4}.'.format(5,31,29,24,16))
print("""
      Days in each month
Jan: {1}    Feb: {0}    Mar: {1}
Apr: {2}    May: {1}   Jun: {2}
Jul: {1}    Aug: {1}    Sep: {2}
Oct: {1}    Nov: {2}    Dec: {1}
""".format(28,31,30))

# String formatting
# use a for loop to output the numbers from 1 to 5 and display their square root and cube.
for i in range(1,16):
    print('No. {0} squared is {1} and cubed is {2}'.format(i, i**2, i**3))
print()

# to properly even each string output or better, even out the lines used the collins format
print('To properly even each string output or better, even out the lines used the collins format.')
for i in range(1,13):
    print('No. {0:2} squared is {1:3} and cubed is {2:4}'.format(i, i**2, i**3))
print()

# right align with this '<' symbol
print('right align with this \'<\' symbol.')
for i in range(1,13):
    print('No. {0:<2} squared is {1:<3} and cubed is {2:<4}'.format(i, i**2, i**3))
print()
# center align with this '^' symbol
print('center align with this \'^\' symbol.')
for i in range(1,13):
    print('No. {0:^2} squared is {1:^3} and cubed is {2:^4}'.format(i, i**2, i**3))
print()

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))



