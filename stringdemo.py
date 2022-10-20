s = "Parthkumar Dasharathbhai Patel"

#for i in s:
#   print(i)
print("*"*50)
for i in range(1):
   print(s)

print(s.capitalize())
print(s.casefold())
print(s.center(50,"*"))
print(s.find("te"))
print(s.endswith("i"))
print(s.startswith("Pa"))
print(s.upper())
print(s.istitle())
print("patel".isalnum())
print("patel123".isalnum())
print("patel 123".isalnum())
print("123".isalpha())
print("123".isdigit())
print("123".isnumeric())
print("hello".replace("l","w"))
print(s.swapcase())
print("parthkumar patel".title())
