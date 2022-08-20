import string
chars = list(string.ascii_lowercase[:10])
print(chars)
x = list(enumerate(chars,1))
for i in x:
    print(i[0],i[1])

#----------

name = 'test'
len(name)
for i in name:
    print(i)

#----------

name = 'test'
len(name)
for i in name:
    print(i + 'Hurray')

#----------

name = 'test'
len(name)
for _ in name:
    print('Hurray')

#----------

lst = [5, 9, 2, 5, 9, 8]
def more_than_five(lst):
    new_lst = []
    for element in lst:
        if abs(element) > 5:
            new_lst.append(abs(element))
    print(new_lst)
    return new_lst
print(more_than_five([6, 2, 11, 3]))

#----------

s = input()
while s == 'end' or s == 'End':
    print(s)
    s = input()

#----------

a = 1
while a < 10:
    print('цикл выполнился', a, 'раз.')
    a += 1
print('Цикл окончен')

#----------

a = 1
while a < 5:
    print('условие верно')
    a += 1
else:
    print('условие неверно')

#----------

a = 1
while a < 20:
    a += 1
    if a == 7:
        break
    print(a)

#----------

a = 1
while a < 25:
    a += 1
    if a == 19 or a == 15 or a == 7:
        continue
    print(a)

#----------

i = 3
while i >= 0:
    print(i)
    i -= 1

#----------

x = 1
while x < 10:
  if x % 2 == 0:
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")

  x += 1

#----------

x = 0
while x <= 20:
    print(x)
    x += 2

#----------

# БЕСКОНЕЧНЫЙ ЦИКЛ
x = 8
while x > 3:
    print(x)

#----------

# БЕСКОНЕЧНЫЙ ЦИКЛ
x = 1
while x == 1:
   print("In the loop")

#----------

x = 0
while x <= 10:
    if x % 2 == 0:
        print(x)
    x += 1

#----------

x = 5
while x > 0:
    print(x)
    x -= 1

#----------

i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break

#----------

i = 0
while i < 5:
  i += 1
  if i == 3:
    print("Skipping 3")
    continue
  print(i)

#----------

i = 0
while True:
    i += 1
    if (i == 2):
        continue
    if (i == 5):
        break

    print(i)

#----------

for i in range(5):
    if i == 0 or i == 4:
        print('-' * 12)
    else:
        print('|' + ' ' * 10 + '|')

#----------

for element in range(1, 10, 3):
    print(element)
    if element <= 1:
        print('Hi')
    else:
        print('Welcome')

#----------

for element in range(1, 11):
    print(element)

#----------

for element in range(10):
    print(element)

#----------

m = 2
n = 10
for element in range(m, n + 1):
    i = int(input())
    if i > 5:
        print(i)
    print(element)
print("m", m)

#----------

s = 'Hello'
s = input()
for i in range(10):
    print(i, s)

#----------

s = 'Hello'
for i in range(1, 11):
    print(i, s)

#----------

n = 6
for i in range(n):
    print('*' * n)
    n -= 1

#----------

n = 6
for i in range(n):
    print('*' * (n - i))

#----------

m = 10
p = 50
n = 6
for i in range(n):
    m = m + m * p / 100
    print(i + 1, m)

#----------

# если положить 1000 долларов в банк на 12 месяцев под проценты
m = 1000
p = 3
n = 12
for i in range(n):
    m = m + m * p / 100
    print(i + 1, m)

#----------

for i in range(3, 15, 2):
            #старт стоп шаг
    print(i)

#----------

m = 5
n = 1
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)

#----------

m = 15
n = 5
for i in range(m, n -1, -1):
    if i % 2:
        if i % 2 == 1:
            if i % 2 != 0:
                print(i)

#----------

x = 0
while x < 10:
    print(x)
    x += 2

#----------

str = input()
while str != 'END':
    print(str)
    str = input()

#----------

str = input()
while str != 'END' and str != 'end':
    print(str)
    str = input()

#----------

s = ['end', 'END', 'End']
n = input()
while n not in s:
    print(n)
    n = input()

#----------

ABC = 'Hello Python!'
ABC_list = list(ABC)
print(ABC_list)
n = len(ABC_list)
print(n)
for i in range(n):
    print(ABC_list[i])

#----------

i = 0
while i < 100:
    i += 1
    if i != 46:
        print(i)
        continue
    break

#----------

for x in range(0, 21, 2):
    print(x)

#----------

for x in range(1, 31, 2):
    print(x)

#----------

ABC = 'abcdefghijklmnopqrstuvwxyz'
ABC_list = list(ABC)
print(len(ABC))
y = 1
for i in range(0, 10):

    print(y, ABC[i])
    y += 1

#----------

for x in range(30, 0, -1):

    print(x)

#----------

my_list = ['test 1', 'test 2', 'test 3']
for x in my_list:
    print(x)

#----------

my_list = ['test 1', 'test 2', 'test 3', 'test 2', 'test 1']
for x in my_list:
    print(x)

#----------

lst = ['one',  'two', 'three']
for el in lst:
    print(el)

#----------

for el in range(len(lst)):
    print(el)
for el in range(len(lst)):
    print(lst[el])

#----------

l = 0
while l < len(lst):
    print(lst[l])
    l += 1

#----------

print(lst.index('one'))

#----------

x5 =[]
for i in range(5):
    x5.append(i)
print(x5)

#----------



























