a = 12
b = 3

print(a + b)  # 15
print(a / b)  # 4.0 returns the float division result
print(a - b)  # 9
print(a * b)  # 36
print(a // b)  # 4 returns the integer division result
print(a % b)  # 0 returns the reminder
print(" ")

# for loop for python. always remember that the "//" is used for integer division and the "/" is used for float division
# for i in range(1,a/b):
# print(i) will not work because you're using one / to divided integers values

for i in range(1, a // b):
    print(i)
