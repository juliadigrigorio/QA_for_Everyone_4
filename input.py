age = int(input())
print(age)

#----------

height = float(input())
print(height)

#----------

name = input()
age = input()
print(name + ' is ' + age)

#----------

temp = int(input())
if temp >= 100:
    print("Boiling")

#----------

age = int(input())
if age >= 18:
    print('Allowed')
else:
        print('Sorry')

#----------

age = int(input())
if(age >= 0 and age <= 11):
    print("Child")
elif(age >= 12 and age <= 17):
    print("Teen")
elif(age >= 18 and age <= 64):
    print("Adult")

#----------

name = input()
print('Hello, ', name)
print(f'Hello, {name}')

#----------

x = int(input())
y = x + 1
print(x,y, sep='\n')

#----------

x = int(input())
y = x + 2
z = y + 2
print(y,z, sep='\n')
if x >= 0:
    print(y,z, sep='\n')
else:
    print('отрицательное я не умею')

#----------

x = int(input())
y = int(input())
z = int(input())

print(x + y + z)

#----------

rebro = int(input())
o = rebro ** 3
p = 6 * rebro ** 2
print(f'Объем: ', o)
print('Площадь: ', p)

#----------

x = int(input())
print(f'Предыдущее число: {x - 1}')
print(f'Следующее число: {x + 1}')

#----------

monitor = int(input())
blok = int(input())
klaviatura = int(input())
mish = int(input())
summa = (monitor + blok + klaviatura + mish) * 3
print(summa)

#----------

population = int(input())
survivors = population // 2 + population % 2
print(survivors)

#----------

x = int(input())
y = int(input())

print(f'summa: {x + y}')
print(f'разность: {x - y}')
print(f'произведение: {x * y}')

#----------

x = int(input())
print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep="---")

#----------

seconds = int(input())
minutes = seconds / 60
hours = seconds / 3600
print(f'Hours:  {hours}, Minutes: {minutes}, Seconds: {seconds}')

#----------

password = input('enter password: ')
confirmation = input('enter confirmation: ')
if password == confirmation:
    print('Accepted')
else:
    print('Declined')

#----------

age = int(input())
if age >= 18:
    print('Access granted')
else:
    print('Access denied')

#----------

mass = float(input('enter your mass: '))
height = float(input('enter your height: '))
BMI = float(mass / (height * height))
if (BMI >= 18.5) and (BMI <= 25.0):
    print('Optimal')
elif BMI < 18.5:
    print('Underweight')
elif BMI > 25.0:
    print('Overweight')

#----------

num = int(input())
if num >= 0 and num < 17:
    print('yes')
else:
    print('no')

#----------

a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))
if a < (b + c) and b < (c + a) and c < (a + b):
    print('ok')
else:
    print('not ok')

#----------

a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))
if a == b == c:
    print('equilateral')
elif (a == b) and (a != c) and (b != c):
    print('isosceles')
elif (a != b) and (a != c) and (b != a) and (b != c) and (c != a) and (c != b):
    print('scalic')

#----------

a = abs(int(input('enter a: ')))
b = abs(int(input('enter b: ')))
c = abs(int(input('enter c: ')))
if a == b == c:
    print('equilateral')
elif (a == b) and (a != c) and (b != c):
    print('isosceles')
else:
    print('scalic')

#----------

y = input('print name: ')

def function_name(_):
    return (f'Hello, {_}')

print(function_name(y))

#----------

g = int(input('numbers: '))
j = int(input('numbers: '))

def funtion_s4et(o,h):
    print(o+h)
funtion_s4et(g,j)

#----------

h = input('your name:  ')
l = int(input('your number:  '))
def function_vizov(a, b):
    print(f'Hello, {a}, your number is {b}')
function_vizov(h, l)

#----------




