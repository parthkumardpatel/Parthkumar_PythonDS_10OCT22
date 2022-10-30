l = [1,2,3,1.1,2.2,3.4,"tops",True,0,1,2,True,False,"Python"]
#    0 1 2  3   4   5     6     7  8 9 0  1     2      3     +
#    4 3 2  1   0   9     8     7  6 5 4  3     2      1     -

print(l)
print()
print(l[1:9])
print(l[:7])
print(l[13:])
print(l[2:5:2])
print(l[::4])
print()

print(l[-4:-12])
print(l[-12:-4])
print(l[:-6])
print(l[-4:])
print(l[-3:-15:-2])
print(l[::-1])
