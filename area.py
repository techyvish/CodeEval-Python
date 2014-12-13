__author__ = 'Vishal'

been_called = True
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

lb = ['x','q','d','r']
lb.sort()
print lb

s = 'spam'
t = list(s)
print t

s = 'pining for the fjords'
t = s.split()
print t

s = 'spam-spam-spam'
t = s.split('-')
print t
r = " ".join(t)
print r

a = 'banana'
b = 'banana'

print a is b

eng2sp = { 'uno':'one', 'ters':'two', 'three':'tres'}
print eng2sp
print eng2sp['ters']
print eng2sp['uno']

def globalTest():
    global  been_called
    been_called = False
    print been_called

globalTest()

t = tuple()
print type(t)

t = tuple('plugin')
print t

addr = 'monty@python.org'
uname,domain = addr.split('@')
print uname,domain

def min_max(t):
    return min(t),max(t)


