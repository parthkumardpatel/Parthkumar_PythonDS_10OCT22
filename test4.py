#Nested if/else
'''
a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))

print("A = ",a," B = ",b," C = ",c)

if a>b:
    if a>c:
        print(a,"Is Greater")
    else:
        print(c,"Is Greater")
elif b>c:
    print(b," Is Greater")
else:
    print(c," Is Greater")
'''

#Ladder if/else

roll_no = int(input("Enter Roll No. "))
name = input("Enter Your Name : ")
s1 = int(input("Enter Physics Marks : "))
s2 = int(input("Enter Chemistry Marks : "))
s3 = int(input("Enter Biology Marks : "))
total = s1+s2+s3
per = total/3
print("Total Marks : ",total)
print("Percentage : ",per)

if per>=75:
    print("Distinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=35:
    print("Pass Class")
else:
    print("Fail")
