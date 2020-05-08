day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
select_day = int(input("Select today's day based on the day array"))
temperature = 30
raining = True
# you can use parenthesis to make the code more clear
if (day[select_day] == 'Fri' and temperature > 27) or not raining:
    print('Go swimming')
else:
    print('Stay at home and learn Python')
print()
# Truth value testing follows 3 principle in python
# constants defined to be false: None & False
# zero of any numeric type
# empty sequences and collections
if '' or {} or 0 or None:
    print('True')
else:
    print('False')
print()
name = input('Please enter your name: ')
if name: # this is equal to name != ''
    print("Hello, {}".format(name))
else:
    print("You don't have a name?")
print()
# the in and not in python rule
s_a = 'South Africa'
letter = input('Enter a character: ')

if letter in s_a:
    print('{} is in {}.'.format(letter,s_a))
else:
    print('That letter is not in {}'.format(s_a))
print()
activity = input('What would like to do today?')

if 'cinema' not in activity.casefold():
    print('But I wanted to go to the cinema')
else:
    print('Great lets go!')