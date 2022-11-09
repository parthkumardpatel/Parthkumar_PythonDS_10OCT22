"""

Dictionary : It works with Key/Value Pair Pattern.
             Every Key is Unique in Dictionary.
             There is no Indexing in Dictionary like List and Tuple.
             It starts from key/value.
             
"""
d={1:"Kamlesh",2:"Mahesh",3:"Parth",4:"Ravi",5:"Rahul"}
print(d)

print(d[5])

d1 = d.copy()
print(d1)
print()

print(d.get(3))

print(d.items())

print(d.keys())

print(d.values())

print(d.pop(5))
print(d)
print(d.popitem())
print(d)

d3 = {4:"Ramesh",5:"Suresh"}
d.update(d3)
print(d)

d[2]="Mangesh"
print(d)

d[5]="Haresh"
print(d)

for i in d:
    # print(d[i])
    print(i,":",d[i])

