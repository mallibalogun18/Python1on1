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
