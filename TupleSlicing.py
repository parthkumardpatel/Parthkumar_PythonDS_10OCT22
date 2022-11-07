#    0 1 2  3   4   5   6     7         8       9   10    11  12  13     14     +
t = (1,2,3,1.1,2.2,3.3,True,"tops",[10,200,300],10,False,1.1,2.2,True,"Python")
#    5 4 3  2   1   0   9     8         7        6   5    4   3   2      1      -

print(t[:])
print(t[:12])
print(t[5:])
print(t[2:14:2])
print()
print(t[-13:])
print(t[-13::-1])
print(t[-1:-7])
print(t[-1:-7:-2])
print(t[::-5])

print()
print(t[1:9])
print(t[:7])
print(t[13:])
print(t[2:5:2])
print(t[::4])

print(t[-4:-12])
print(t[:-6])
print(t[-4:])
print(t[-3:-12:-2])
print(t[::-1])
