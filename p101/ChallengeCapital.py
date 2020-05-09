quote = """Alright, but apart from the Sanitation, 
the Medicine, Education, Wine, Public Order, 
Irrigation, Roads, the Fresh-Water System, 
and Public Health, what have the Romans 
ever done for us? """
# first create a variable that will store all the separators from the quote variable
separators = ''
# for loop through the quote variable and remove all the seperators
for word in quote:
    if word == "," or word == ' ' or word == '?' or word == '-':
        separators = separators + word

# print(separators) this will print out all the separators in the quote

# store each word in the values array
values = "".join(word if word not in separators else " " for word in quote).split()

# If any word starts with a capital letter, print it out.
for i in range(values.__len__()):
    if values[i][0].isupper():
        print(values[i][0])
