file = open('text.txt', 'r')
print(file.read()) # читает весь текст

print(file.read(4)) # читает по символам

print(file.readline()) # читает первую строку
print(file.readline())# читает вторую строку

# ИЛИ

for line in file:
    print(line)

#----------

file.close() #закрыть файл когда закончили с ним работать

#----------

file = open('text.txt', 'a') # добавить в файл (a = append)
file = open('text.txt', 'w') # писать в файл (w = write)
file = open('text.txt', 'x') # создать файл

#----------

#создать, написать, прочесть
file = open('test_1.txt', 'w')
file.write('my super text')
file.close()
file = open('test_1.txt', 'r')
print(file.read())
file.close()

#----------

with open('test_1.txt', 'r') as file: # with закроет файл сам
    print(file.read(4))

#----------

with open('test_1.log', 'w') as file: # создаем лог файл
    file.write('my first log file')

#----------

file = open('texttext.txt', 'w')
file.write('this is my texttext',)
file.close()
file = open('texttext.txt', 'r')
print(file.read())
file.close()

# или
with open('texttext.txt', 'r') as file:
    print(file.read())

#----------

file = open('texttexttext.txt', 'w')
file.write('Hello, Python! Lesson 7')
file.close()
file = open('texttexttext.txt', 'r')
print(file.read())
file.close()

file = open('texttexttext.txt')
my_string = file.read()
print(my_string)
my_new_string = my_string.replace('e', '0')
print(my_new_string)
file.close()
file = open('texttexttext.txt', 'w')
file.write(my_new_string)
file.close()

#----------

my_file = open('text.txt','r')

print(my_file.read())
print(my_file.readline())
print(my_file.readline())

print(my_file.readlines())
print(my_file.readline(3)) # 3 символа
print(my_file.read(3))

for i in my_file:
    print(i)

my_file.close()

#----------

my_file = open('text2.txt', "a") # a = append,т дозаписывает, добавляет.
my_file.write('\n my 3 text')
my_file.close()
my_file = open('text2.txt', 'r')
print(my_file.read())
my_file.close()

#----------

my_file = open('text3.txt', 'x') #х создает файл
my_file.write('some text')
my_file.close()
my_file = open('text3.txt', 'r')
print(my_file.read())
my_file.close()

#----------

import os #удалить файл

my_file = open('text4.txt', "a")
my_file.write('\n my 3 text')
my_file.close()
my_file = open('text4.txt', 'r')
print(my_file.read())
my_file.close()

os.remove('text4.txt') #удалить файл

#----------


