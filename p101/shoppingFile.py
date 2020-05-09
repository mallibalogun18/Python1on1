cart_list = ['milk', 'coke', 'rice', 'bread', 'water']

# continue allows you to skip
for item in cart_list:
    if item == 'rice':
        continue
    print("Buy {}".format(item))  # Buy milk, Buy coke, Buy bread, Buy water will be the output
print()
# This is equivalent to the code below
# for item in cart_list:
#     if item != 'rice':
#         print("Buy {}".format(item))

# Break statement will break the code at a certain value
for item in cart_list:
    if item == 'bread':
        break
    print("Buy {}".format(item))  # Buy milk, Buy coke, Buy rice will be the output

# print out the index where the country stored in the item_to_find variable is located in the country list
country = ['Algeria', 'Nigeria', 'Italy', 'Jamaica', 'Morocco', 'Ghana']
item_to_find = 'Jamaica'
found_at = None
print()
# you can also find the length by rapping the variable in the len() function
# for index in range(country.__len__()):
#     if country[index] == item_to_find:
#         found_at = index
#         break

# the code above is what most program like java would require to do
# python is a rich language and in just 2 steps you can find where the element is located in the list
if item_to_find in country:
    found_at = country.index(item_to_find)
if found_at is not None:
    print("The item was found at position {}.".format(found_at))
else:
    print('{} not found'.format(item_to_find))
