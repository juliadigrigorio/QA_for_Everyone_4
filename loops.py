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

