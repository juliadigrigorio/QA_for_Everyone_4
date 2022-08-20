def approx_equals(a,b):
    diff = abs(a-b)
    return diff <= 0.001

#----------

spisok1 = [5, 2, 6, 8]
spisok2 = [1, 2, 5, 10]

def change(var):
    var = spisok1
    temp = var.pop()
    var.insert(0, temp)
    temp = var.pop(1)
    var.append(temp)

    return var

print(change(spisok1))
print(change(spisok2))

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

arg1 = [4,10,10,9]
def two_highest(arg1):
    new = list(set(arg1))
    new_sorted = sorted(new)
    new_reversed = new_sorted[::-1]
    if len(new_sorted) > 2:
        return  print(new_reversed[0:2])
    else:
        return print(new_reversed)
two_highest(arg1)

#----------

arg1 = [4,10,10,9]
def two_highest(arg1):
        arg1 = list(set(arg1))
        arg1 = sorted(arg1)
        arg1.reverse()
        return print(arg1[0:2])
two_highest(arg1)

#----------

def devide(a, b):
    return a / b
a = 6
b = 2

print(devide(a,b))

#----------

def int_to_string(a):
    return str(a)

print("Function test: " + int_to_string(123))

#----------

def my_function():
    x = int(input('1:'))
    y = int(input('2:'))
    if x >= 6 or y <= 9:
        print('k')
    else:
        print('kaka')

my_function()

#----------

def inc_function(x,y):
    print(x + y)

inc_function(4,6)

#----------

def my_function(x, y):
    z = (x + y) / 2
    text = f' Result of the calculation: {z}'
    print(text)
a1 = 14
b1 = 23
my_function(a1, b1)

#----------

def sum_function(x, y):
    result = x + y
    return result

a1 = 14
b1 = 23
res = sum_function(a1, b1)
print(f'result: {res}')

#----------

def compare(x, y):
    if x > y:
        return True
    else:
        return False

print(compare(3, 4))

#----------

def compare(x, y):

    if x > y:
        return x
    else:
        return 0

print(compare(6,  4))

#----------
# GLOBALNIE I LOKALNIE PEREMENNIE
x = 45

def dummy():

    x = 12
    x += 1
    print(x)

dummy()
print(x)

#----------

x = 45

def dummy():
    global x
    x = 12
    x += 1
    print(x)

dummy()
print(x)

#----------

x = 45

def dummy():
    x = 12
    x += 1
    return x

dummy()
print(x + dummy())

#----------

''' 1) Write a function to compare 2 numbers.
	E.g. compare(2, 3) should return False otherwise should return True.
'''

def my_function(x, y):
    if x == y:
        return True
    else:
        return False

print(my_function(3, 4))

#----------

''' 2) Modify the previous function to compare only positive numbers.
	In case of negative numbers it will return a print statement like: "Can compare only positive numbers!".
'''

def compare_positive(x, y):
    if x > 0 and y > 0:
        print('ok')
    else:
        print('Can compare only positive numbers!')
    if x == y:
        return True
    else:
        return False
print(compare_positive(3, 2))

#----------

''' 3) Write a function to sum 2 numbers.
	E.g. add(4, 5) should return 9 as a result.
'''
def sum_function(x, y):
    result = x + y
    return result
print(sum_function(4,5))

#----------

'''4) Write a function to subtract 2 numbers.
	E.g. sub(4, 2) should return 2 as a result.
'''
def subtract_function(x,y):
    result = x - y
    return result

print(subtract_function(4,2))

#----------

''' 5) Write a function that returns a type of input.
	E.g. give_a_type("test") should return a print statement like: "string".
'''
def type_function():
    x = input()  # у input type всегда string
    return type(x)

#----------

''' 6) Write a function that prints input vertically.
    E.g.print_vertical("test me please")
'''

def vertical_function():
    x = list(input())
    for i in x:
        print(i)


vertical_function()

#----------

''' 7) Write a function that concatenates 2 strings.
 	E.g. concat("abc" , "123") should return a print statement like: "adc123".
'''

def concatenate_function(x, y):
    result = x + y
    return result

print(concatenate_function('fgh', '456'))

#----------

y = input('print name: ')

def function_name(_):
    return (f'Hello, {_}')

print(function_name(y))

#----------

h = input('your name:  ')
l = int(input('your number:  '))
def function_vizov(a, b):
    print(f'Hello, {a}, your number is {b}')
function_vizov(h, l)

#----------

def calculate(a,b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '*':
        if b != 0:
            return a / b
        else:
            return 'Not allowed'

    else:
        'Invalid operation'

def capitalize_every_word(string):
    return string.title()

#----------



