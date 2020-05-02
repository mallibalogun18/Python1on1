a = 12
b = 3

print(a + b)  # 15
print(a / b)  # 4.0 returns the float division result
print(a - b)  # 9
print(a * b)  # 36
print(a // b)  # 4 returns the integer division result
print(a % b)  # 0 returns the reminder
print()
# Always remember that the "//" is used for integer division and the "/" is used for float division
# for i in range(1,a/b):
# print(i) will not work because you're using one / to divided integers values
for i in range(1, a // b):
    print(i)

# EXERCISE
# You just enrolled in E-trade and you have deposit 1500 dollars. You looking at shares to buy and you see that
# the DKNG (Draft King) stock is worth 19.40 a share. How many share can you buy. The output should be of a whole number
accountBalance = 1000
DKNGstock = 19.40
output = 1000 // 19.40
print()
# Something that you should also keep in mind. Unlike java, you can't concatenate strings with other data types.
# You can resolved that by using the str() function.
print("With 1000 dollars I can buy " + str(output) + ' shares.')
print()
# examples of float and int functions in action.
print(float(10))
print(int(10.4))
print()
# arithmetic in python
print((a+b)/3-(4*12))
print(a+b/3-4*12)