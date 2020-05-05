# interpolation in python %d for int, $f for floats, %s for strings
age = 21
print("My age is %d years"%age)
print()
name = 'James Brown'
liveAlbum = 15
pi = 22/7

print("%s has recorded %d Live albums."%(name, liveAlbum))
print("Pi is approximately %f"%pi)
print()
# like other programming languages, in between the % and f
# you can use the '.' follow by a number to determine how many number after the decimal you want the output to show
# or better the precision of the number.
print("Pi is approximately %.2f"%pi)
print("Pi is approximately %.50f"%pi)
print("Pi is approximately %.10f"%pi)
print("Pi is approximately %.4f"%pi)
