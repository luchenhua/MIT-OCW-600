__author__ = 'luchenhua'

x = 3
x = x * x
print x

y = raw_input('Enter a number: ')
print type(y)
print y

y = float(raw_input('Enter a number: '))
print type(y)
print y
print y * y

x = int(raw_input('Enter an integer: '))
if x % 2 == 0:
    print 'Even'
else:
    print 'Odd'
if x % 3 != 0:
    print 'And not divisible by 3'

x = int(raw_input('Enter x: '))
y = int(raw_input('Enter y: '))
z = int(raw_input('Enter z: '))

if x < y:
    if x < z:
        print 'x is least'
    else:
        print 'z is least'
else:
    print 'y is least'

if x < y:
    if x < z:
        print 'x is least'
    else:
        print 'z is least'
elif y < z:
    print 'y is least'
else:
    print 'z is least'

if x < y and x < z:
    print 'x is least'
elif y < z:
    print 'y is least'
else:
    print 'z is least'
