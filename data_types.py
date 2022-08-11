string_1 = 'ololo'
x=10
y=14
z=5
print(x+y-z)
print(x/z*y)

#----------

print(type(x))
print(type(string_1))

#----------

print(round(2.7))

#----------

import math

print(math.ceil(2.3))
print(math.floor(2.3))
print(abs(-28))
print(4 ** 4 ** 4)
print(int('42'))

#----------

from decimal import Decimal

number = Decimal('0.01')
number = number + 2
print(number)
print(round(Decimal('2.5')))

#----------

from fractions import Fraction

number = Fraction(10, 7)
print(number)
print(int(number))
print(Decimal(2.5))

#----------

from math import *

print(3 + 3.0 + 4)
a = 1.9
print(trunc(a))
print(type(a))
b = trunc(a)
print(type(b))
print(float(0))
s = 23.0
print(s.is_integer())
print(s == int(s))

#----------

up = '6'
ip = '7'
print('/'.join(up + ip))

#----------

x = 4
x += 5
print(x)

#----------

print(8/2)
print(6*7.0)
print(4+1.65)
print(8**(1/3))
print(20%6)

#----------

a = 1
b = 2
c = 3

print(a, b, c, sep='*')

#----------

a = 1
b = 2
c = 3

print(a, b, c, sep='*', end='***')

#----------

x = int(input())
y = x + 1
print(x,y, sep='\n')

#----------



