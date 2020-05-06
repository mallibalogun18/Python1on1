my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#         -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# the way to read list = list[start:end:step]

# when printing a slice list with a start and end element the value at end element is never displayed
print(my_list[1:-2])  # [1, 2, 3, 4, 5, 6, 7]
print(my_list[-2:-7])  # this will output nothing because in python
print()
# (and in any programming language) you can't go backwards
# to get a better grasp to what's taking place above look at the below output
print(my_list[4:2])  # if the start index is at 4 you can only output element after 4.
# for that reason, this will also output an empty array
print()
# when slicing and you want to output the end of the list, you don't have to put the end value
print(my_list[4:])  # [4, 5, 6, 7, 8, 9]
# vice versa, you don't have to type the begging of an array, but just remember which ever value is at the end
# element will not be outputted
print(my_list[:5])  # [0, 1, 2, 3, 4]
print()
# the same principle apply when using negative integers.
print(my_list[:-7])  # [0, 1, 2]
print(my_list[-7:])  # [3, 4, 5, 6, 7, 8, 9]
# when utilizing or better inserting the step index we are telling the program to output the step index from the
# start to end of that variable.
# so if we wanted to output every second value of the my_list variable starting from the index at 1
print()
print("The variable my_list values second value starting at index 1 are {0}".format(my_list[1::2]))



# lets apply the same principles when using strings
# when programming its always good to say things out loud and visualize a
# string in an index format
my_string = 'Mon,Tue,Wed,Thu,Fri,Sat,Sun'
# 0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32
# by slicing the variable my_string, output all the comas in the string
print(my_string[3::4])  # This will output all the comas. Locate the first coma and that will be your start
# Next, since we want to output all the coma there's no need for an end.
# lastly, you can notice there's a pattern with the coma. Determine how many index will it take to get to the next coma.
# in this case is every 4th index.
# DO the same now and display the first letter of each day.
print()
print(my_string[::4])  # The output will be MTWTFSS and the rules remain the same
# CHALLENGE
# can you perform the same task and output the same value by using negative integers
# first thing first I will determine the length of the string by using the len function
print()
print(len(my_string))  # the string is 27 digit long meaning there will be the index 0 to 26
# and for the negative value will be -1 to -27
# in the my_string variable the index -1 represents the end of the string 'n' and the index -27 represents 'M'
print()
print(my_string[-1])  # n
print(my_string[-27])  # M
# now that I know my 'coordinates', cause that's what's taking place I can output the first letter in each day
# by using nevative integers
print()
print(my_string[-27::4])  # MTWTFSS
# now I am sure you've realized that we didn't have to go through this process to come with this result. The only
# thing that change is we replace the start from 0 (which we didn't declare in the first exercise) to
# -27, but I think it's always a great exercise to think through a process when you first begin programming
# or learning a new language. Especially when you ready for job interviews. You want to be able to exaplain what you're
# doing. Hope this helps somebody.
