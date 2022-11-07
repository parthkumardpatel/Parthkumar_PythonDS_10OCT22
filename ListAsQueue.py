# Queue : It follows FIFO (First in First Out)
#       e.g. Ticket Booking System (Train/Bus)

from _collections import deque

l = deque([])
l.append(10)
print(l)

print(list(l))

l.append(20)
print(list(l))
l.append(30)
print(list(l))
l.append(40)
print(list(l))
l.append(50)
print(list(l))

l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
