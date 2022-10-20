s1 = "String Slicing"

#    012345678901234567    +
s = "Python Programming"
#    876543210987654321    -

print(s1.center(50,"*"))
print()
print(s)
print()
print("*"*50)
print("For Positive Slicing")
print("*"*50)
print(s[1:10])
print(s[:8])
print(s[6:14])
print(s[2:17:2])
print(s[::4])
print()
print("*"*50)
print("For Negative Slicing")
print("*"*50)
print()
print(s[-17:-1])
print(s[:-15])
print(s[-15:])
print(s[-12:-4:2])
print(s[::-1])
print(s[-1:-18:-1])
print(s[-1::-2])
print(s[-1:-16:-3])
