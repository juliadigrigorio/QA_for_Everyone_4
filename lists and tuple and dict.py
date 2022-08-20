my_list = [1, 2, "something", True, 4.0]
print(my_list[3])
print(my_list)

#----------

s = 'a,b,c'
print(s.split())

#----------

w = [1, 3, 5, 6, 7]
print(type(w))
w.reverse()
print(w)

#----------

d = ['s', 'd', 'f']
d.reverse()
print(d)

#----------

str1 = "ass"
list1 = list(str1)
list1.reverse()
print(list1)

#----------

t = [1, 2, 3, 4, 5]
print(t)
print(t[::-1])
print(t)

#----------

spisok3 = [15,12,13,56]# meniaet mestami perviy i oisledniy elementi spiska BEZ FUNKCII
first = spisok3.pop()
spisok3.insert(0, first)
last = spisok3.pop(1)
spisok3.append(last)

print(spisok3)

#----------

import string
chars = list(string.ascii_lowercase[:10])
print(chars)
x = list(enumerate(chars,1))
for i in x:
    print(i[0],i[1])

#----------

lst = [7, 8, 5, 9]
lst[0] = 6
print(lst)

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

l = [1,2,3,4,]
def reverse_list(l):
    l.reverse()
    print(l)
    return
reverse_list(l)

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

ABC = 'Hello Python!'
ABC_list = list(ABC)
print(ABC_list)
n = len(ABC_list)
print(n)
for i in range(n):
    print(ABC_list[i])

#----------

ABC = 'abcdefghijklmnopqrstuvwxyz'
ABC_list = list(ABC)
print(len(ABC))
y = 1
for i in range(0, 10):

    print(y, ABC[i])
    y += 1

#----------

my_list = [1,2,5,'r', True,1,2,5]
my_list.append('khgk')
print(my_list)
my_list.pop(1)
print(my_list)
my_list.insert(0,1)
print(my_list)
my_list.append([45.1, 56778])
print(my_list)
my_list.insert(0, [123445, 5.6])
print(my_list)
my_list.insert(-1, ('book', 'look'))
print(my_list)
print(my_list[3])

#----------

my_dict = {
    'key': 'value',
    'book_name': 'Tom Soyer',
    'Author': 'Mark Tven',
    'Date': 1922,
    'is new': True,
    1: ['yes', 'no']
}
my_dict['Date'] = 2023 #переприсвоить значение
print(my_dict)

print(my_dict['is new']) #найти элемент по ключу

my_dict['jortgv'] = 2 #добавить новый ключ и значение
print(my_dict)

my_dict[('nhfgcnh')] = ['ngvg',987,653] #добавить новый элемент с ключем tuple и значением список
print(my_dict)

print(my_dict['Date']) #получить элемент по ключу

my_dict.pop('Date') #удалить элемент
print(my_dict)

print(my_dict.keys()) #  получить список ключей
print(my_dict.values()) # получить список values

#----------

my_list = ['test 1', 'test 2', 'test 3']

print(my_list[0])
print(my_list[1])
print(my_list[2])

#----------

my_list = ['test 1', 'test 2', 'test 3']
for x in my_list:
    print(x)

#----------

my_list = ['test 1', 'test 2', 'test 3', 'test 2', 'test 1']
for x in my_list:
    print(x)

#----------

my_list = ['test 1', 'test 2', 'test 3', 'test 2', 'test 1']
print(my_list)

my_list[0] = 1024
my_list[3] = False

print(my_list)

#----------

my_list = ['test 1', 'test 2', 'test 3', 'test 2', 'test 1']
print(len(my_list))
print(type(my_list))

#----------

my_list = ['test 1', 'test 2', 'test 3', 'test 2', 'test 1']
print(my_list)
my_list.append(-5435)
print(my_list)

#----------

# в отличие от списка картеж нельзя изменить
# TUPLES (картеж)

my_tuple = ('test1', 'test2', 'test3')
print(my_tuple[1])

#----------

my_tuple = (1234, 'test1', 'test2', 'test3')
print(my_tuple)
my_tuple[0] = 'gogogo'  #попытка изменить tuple
print(my_tuple)

#----------

my_list = [1234, 'test1', 'test2', 'test3']
my_tuple = (1234, 'test1', 'test2', 'test3')
print(my_tuple)
print(my_list)
my_list[0] = 'changed'
print(my_list)
my_list.append(True)
print(my_list)

#----------

#СЛОВАРИ.      КЛЮЧИ ДОЛЖНЫ ЮЫТЬ УНИКАЛЬНЫ. типы данных мб разными. Индекс не присваевается.

my_dictionary = {
    'name': 'John',
    'Last_name': 'Doe',
    'BOB': '2022-03-21',
    'Note': 'likes python'
}
print(my_dictionary)
my_dictionary['name'] = 'Johanne'
print(my_dictionary)

#----------

my_dictionary = {
    'name': 'John',
    'Last_name': 'Doe',
    'BOB': '2022-03-21',
    143: 'likes python',
    'name': 'jojo'
}
print(my_dictionary)
my_dictionary['name'] = 'Johanne'
print(my_dictionary)
print(my_dictionary['Last_name'], my_dictionary[143])
print(len(my_dictionary))

#----------

my_dictionary = {
    'name': 'John',
    'Last_name': 'Doe',
    'BOB': '2022-03-21',
    143: 'likes python',
    'colors': ['red', 'yellow', 'white', 'etc.']
}
print(my_dictionary['colors'])

#----------

# МНОЖЕСТВО данные в них не отсортированы. Не содержит копии.

my_set = {'element_1', 'element_2', 'element_3', 'element_2', 'element_2', 'element_2'}
print(my_set)
print(len(my_set))
print(type(my_set))

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

x1 = [1,2,3]
x2 = [4,5,6]
print(x1 + x2)

#----------

x3 = '1,2,3,4,5'
x4 = (list(x3))
print(x4)

#----------

x5 =[]
for i in range(5):
    x5.append(i)
print(x5)

#----------






