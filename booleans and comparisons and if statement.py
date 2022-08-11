a=2
b=3
print(a==b)

#----------

x = 8
y = 6
if x > y:
    print('True')
else:
    print('False')

#----------

x = 3
y = 6
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is less than {y}')

#----------

x = 0
y = 6
if (x == 0) or (y == 0):
    print('One or both numbers are not positive, can\'t proceed with the comparison!')
elif (x > 0) and (y > 0) and (x > y):
    print(f'{x} is greater than {y}')
elif (x > 0) and (y > 0) and (x < y):
    print(f'{x} is less than {y}')

#----------

op = 'ella'
print('*'.join(op))
op1 = "*".join(op)
char = op1.split('*')
print(char)
char.reverse()
print(char)
op3 = "".join(char)
if (op == op3):
    print("palindrome")
else:
    print("NOT palindrome")

#----------

print(7 != 8)

#----------

t = 8
b = 42
if b > t:
    print('hello')

#----------

num = 7
if num > 3:
   print('3')
   if num < 5:
      print('5')
      if num == 7:
         print('7')

#----------

temp = int(input())
if temp >= 100:
    print("Boiling")

#----------

x = 'a'
if (x < 'c'):
    x += 'b'
if (x > 'z'):
    x += 'c'

print(x)

#----------

grade = 5
if grade >= 75:
    print('Passed')
else:
    print('Failed')

#----------

num = 3
if num == 1:
  print("One")
else:
    print('something')
    if num == 2:
        print('dva')
    else:
        print('something')
        if num == 3:
            print('tri')
        else:
            print('net')

#----------

x = 10
y = 20
if x > y:
    print('if statement')
else:
    print('else statement')

#----------

num = 8
if num == 1:
  print("One")
elif num == 2:
  print("Two")
elif num == 3:
  print("Three")
else:
  print("Something else")

#----------

age = int(input())
if age >= 18:
    print('Allowed')
else:
        print('Sorry')

#----------

if not True:
   print("1")
elif not (1 + 1 == 3):
   print("2")
else:
   print("3")

#----------

country = "US"
age = 42

if(country == "US" or country == "GB") and (age > 0 and age < 100):
  print("Cool")

#----------

age = int(input())
if(age >= 0 and age <= 11):
    print("Child")
elif(age >= 12 and age <= 17):
    print("Teen")
elif(age >= 18 and age <= 64):
    print("Adult")

#----------

def print_s(s):
    print(type(s))
    if str(type(s)) == "<class 'str'>":
        print(s[1])
        print('Hooray')
    else:
        print('invalid parameter')
st = 'dfdhbjh'
print_s(st)

#----------

num = 10
if num == 0:
    print('yes')
else:
    print('no')

#----------

password = input('enter password: ')
confirmation = input('enter confirmation: ')
if password == confirmation:
    print('Accepted')
else:
    print('Declined')

#----------

number = int(input())
if number % 2 == 0:
    print('even')
else:
    print('odd')

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

num = int(input())
if -2 >= num > -30 or 7 < num <= 25:
    print('ok')
else:
    print('no')

#----------

num = int(input())
if num > -30 and num <= -2:
    print('ok')
elif num > 7 and num <= 25:
    print('ok')
else:
    print('not ok')

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


