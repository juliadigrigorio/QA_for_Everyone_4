my_list = [1, 2, "something", True, 4.0]
print(my_list[3])
print(my_list)

s = 'a,b,c'
print(s.split())

w = [1, 3, 5, 6, 7]
print(type(w))
w.reverse()
print(w)

d = ['s', 'd', 'f']
d.reverse()
print(d)

str1 = "ass"
list1 = list(str1)
list1.reverse()
print(list1)


t = [1, 2, 3, 4, 5]
print(t)
print(t[::-1])
print(t)

spisok3 = [15,12,13,56]# meniaet mestami perviy i oisledniy elementi spiska BEZ FUNKCII
first = spisok3.pop()
spisok3.insert(0, first)
last = spisok3.pop(1)
spisok3.append(last)

print(spisok3)


