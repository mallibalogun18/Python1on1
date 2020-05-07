# IF Statement
print("If statement Program challenge")
your_name = input("Hello, what is your name? ")
# so whenever you're asking for the user to insert an int value make sure to wrap the input() function inside of the
# int function whenever we want the value to rapresent a string
your_age_int = int(input(f"{your_name} how old are you?"))
# your_age_str = input(f"{your_name} how old are you?")
print()
# print(type(your_age_int)) # the variable your_age_int is a of type int
# print(type(your_age_str)) # the variable your_age_str is a of type str
print()
if your_age_int >= 18:
    print("""As a {0} year old, you're old enough to vote.""".format(your_age_int))
    print("You may select the candidate of your choosing by X one of the boxes.")
else:
    print(("""You're not old enough to vote. Please come back in {0} years.""".format(18 - your_age_int)))
print()
# Elif aka Else if in other programming languages i.e. Java
print("Elif statement Program challenge")
num_select = int(input('Select a number between 0-9: '))
print()
if 0 <= num_select <= 2:
    print("The number you selected is between 0 and 2")
elif 3 <= num_select <= 6:
    print('The number you selected is between 3 and 6')
elif 7 <=num_select <= 9:
    print('The number you selected is between 7 and 9')
else:
    print('Your selection was not a number between 0-9')

# IF-ELIF exercises
# Write a small program that assigns the name of 2 trees to 2 variables, called tree1 and tree2 If the values of the
# 2 variables are equal, print the message 'The trees are the same', otherwise print 'The trees are different'. This
# exercise system doesn't allow input to be used, so don't use input on lines 1 and 2 - just enter your text inside
# the quote for the trees.
tree1 = 'Aspen'
tree2 = 'Hawthorn'

# add the code to compare the trees
if tree1 == tree2:
    print('The trees are the same')
else:
    print('The trees are different')

print()
# Write a small program that assigns the value 5 to one variable called x and value 7 to a variable called y. Use the
# if statements to compare the values and print out 'x is greater than y' if x is greated, or 'x is smaller than y'
# +
# if y is greater, and if x equals y, print out 'x equals y'.

x = 5
y = 7
if x > y:
    print('x is greater than y')
elif x < y:
    print('x is smaller than y')
elif x == y:
    print('x equals y')