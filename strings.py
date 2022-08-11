print("hello world!")

#----------

string='some "text" here'
print(string)

#----------

x=10
y=7
print(x-y)
#----------

string_0 ='Hello World!'
print(string_0)

#----------

string_1 ='Good'
string_2 =' Morning'
print(string_1, string_2)

#----------

print('Hello QAForEveryone!')
string_3 = 'Hello QAForEveryone!'
print(string_3)

#----------


a='------------'
b='|   *  *   |'
c='|          |'
d='|   ____   |'
e='------------'
print(a)
print(b)
print(c)
print(d)
print(e)

#----------

print('Python is cool')
str ='Python is cool'
print(str)

#----------

print(' '*6 +'*')
print(' '*4 +'*'*4)
print(' '*2 +'*'*8)
print(' ' +'*'*10)
print(' '*5 +'*')

#----------

print('_'*10)
print('|',' '*6,'|')
print('|',' '*6,'|')
print('|',' '*6,'|')
print('-'*10)

#----------

print('_'*10+'\n'+'|',' '*6,'|'+'\n'+'|',' '*6,'|'+'\n'+'|',' '*6,'|'+'\n'+'-'*10)

#----------

print('it\'s a dog')

#----------

print('a\
      b\
      c\
      d')

#----------

print('foo \t bar')

#----------

s = 'a,b,c'
print(s.split())

#----------

r = 'my name is ffff'
print('ffff' in r)
print('iii' in r)
print('ffff' not in r)

#----------

print(len(r))
t = ''
print(len(t))
print(len(t) > 0)

#----------

z = 'my name is xxxx'
print(z.replace('x', 'y'))

#----------

x = -5
print(x.__abs__())

#----------

str1 = "yYyy"
print(str1.replace("Y", "Z"))

#----------

s = 'something'
print(s.upper())

#----------

m = 'SOMETHING'
print(m.lower())

#----------

f = 'this is a new day'
print(f.capitalize())
print(f.title())
print(f.swapcase())
print(f.startswith('t'))
print(f.endswith('y'))

#----------

str1 = "ass"
list1 = list(str1)
list1.reverse()
print(list1)

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


print(f'jklgf{456}')

#----------

print('One\tTwo\tThree')
print('''One
Two
Three''')

#----------


string = '''jfjgfhjgfhj
 ghjgfdhjgdfhjgdhjgd
 hgfjhgdfhjgdjhdhjgd'''

print(string)

#----------

print('Brian\'s mother said: \"He is ok"')

#----------

print('-' * 12)
print(('|' + '  ' * 5 + '|'), ('|' + '  ' * 5 + '|'), ('|' + '  ' * 5 + '|'), sep='\n')
print('-' * 12)

#----------

name = input()
print('Hello, ', name)
print(f'Hello, {name}')

#----------

x = int(input())
y = x + 1
print(x,y, sep='\n')

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

name = 'Julka'
age = 20
msg = 'My name is %s and my name is %s' % (name, age)
print(msg)

#----------

name = 'Julka'
age = 20
msg = 'My name is {} and my age is {}'
print(msg.format(name, age))

#----------

name = 'Julka'
age = 20
msg = f'My name is {name} and my age is {age}'
print(msg)

#----------

# vivesti alfavit
import string
s = string.ascii_lowercase
print(s)

#----------

a = 43
b = 10
c = 5
total_goals = a + b +c
print ("total goals: " + str(total_goals))
print(f'total goals: {total_goals}')

#----------

def greet(name):
    return f"Hello, {name}, how are you?"

print(greet("Bill"))

#----------






