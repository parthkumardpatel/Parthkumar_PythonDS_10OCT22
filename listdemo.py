s = "List Demo"
l = [1,2,3,1.1,2.2,3.3,"Python",True,1,2,False,"Tops",True,0]
print(s.center(80,"*"))
print()
print(l)

l.append(300)
print(l)

l1 = l.copy()
print(l1)

l2 = l
#l2 = l.copy()
#print(l2)

l1.append(200)
print(l1)

l2.append(400)
print(l2)
print(l)

l.pop()
print(l)

l.remove("Tops")
print(l)

l.reverse()
print(l)

l.insert(3,1001)
print(l)

print(l.count(1))
print(l.count(0))

l2 = [43,54,21,56,23,64]
l2.sort()
print(l2)

print()
l3 = [1001,2001,3001]
print(l3)


l.extend(l3)
print(l)
print(l.index(2001))
l.insert(8,"Parth")
print(l)
l.remove(1001)
print(l)
#l.clear()
#print(l)

l.reverse()
print(l)

for i in l:
    print(i)
print(4001 in l)
print("Parth" in l)
