parrot = "Norwegian Blue"
print(parrot)
print()
# Mini Challenge
# Add some code to the program, so that it prints out "We Win". Each character should appear on a separate line.
# The program should get the characters from the parrot string, using indexing.
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()
# Mini Challenge
# Perform the above mini challenge, but this time use negative indexing
print('Output using negative indexing')
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()
# a quicker way to use the negative indexing without counting their position is to subract the lenght of the string
# by the array number from the first exercise
print('Output using string indexing minus the length of the string')
print(parrot[3-14])
print(parrot[4-14])
print(parrot[9-14])
print(parrot[3-14])
print(parrot[6-14])
print(parrot[8-14])