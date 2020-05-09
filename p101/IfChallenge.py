# Write a small program to ask for a name and an age. When both values have been entered, check if the person is the
# right age to go on an 18-30 holiday (they must be over 18 and under 31). If they are welcome them to the holiday,
# otherwise print a (polite) message refusing them entry. Our programs expect valid input. We'll see how to handle
# invalid numbers, later in the course.

person_name = input("pleae, Enter your name: ")
person_age = int(input("Enter your age"))

if 18 <= person_age < 31:
    print("Hello {}, welcome to the 18-30 holiday party!!".format(person_name))
else:
    print("Sorry, but you aren't eligible to attend the holiday party.")

