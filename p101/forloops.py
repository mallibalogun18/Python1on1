us_states = ['Illinois','New York','Alabama','Florida','Puerto Rico','Texas','California']
for i in range(us_states.__len__()):
    print(us_states[i])
print()
name = 'James Brown'
for i in name:
    print(i)
print()
# This code was taken from the Slicing.py class. Let's analyze what's occurring
num1 = '9,223;372:036 854,775;807'

num = input("Please enter a series of numbers using any separators you like: ")
separators = num[1::4]
sep = ''
for char in num:
    if not char.isnumeric():
        sep = sep + char
print('This will print all the separator in the num variables base on the slice')
print(sep)
print()

values = "".join(char if char not in sep else " " for char in num).split()

print(values)
print([int(val) for val in values])
