"""

Tuple : It contains group of data like List.

1) In Tuple, we use : ()
2) In List, we use  : []
3) In list : you can change at runtime.
4) In Tuple: you cannot change at runtime.

"""

t = (1,2,3,1.1,2.2,3.3,True,"tops",[10,200,300],10,False,1.1,2.2,True,"Python")
print(t)

print(t.index(10))
print(len(t))
print(t.count(1))
print(t.count(0))

print(t[8])
t[8].append(400)
print(t[8])
t[8].append(500)
print(t[8])
print(t)

for i in t:
    print(i)

print("tops" in t)
print("to" in t)

