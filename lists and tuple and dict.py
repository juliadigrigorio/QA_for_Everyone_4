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


