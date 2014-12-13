__author__ = 'Vishal'

import  math
def area(radius):
    temp = math.pi * radius**2
    return temp

print area(100)

def distance(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y2
    dsqured = dx**2 + dy**2
    return dsqured

print distance(10, 10, 100, 100)


prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print letter + suffix

s = 'Monty Python'
print s[0:5]
print s[6:12]
s = 'banana'
print s[3:]
print s[:3]

l = ['a','b','c','d']
l.append('e')
c = ['f','g']
l.extend(c)
print l


