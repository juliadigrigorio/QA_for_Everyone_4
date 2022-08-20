class Animal:
    def __init__(self, name):
        self.name = name
        self.weight = 0

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self). __init__(name)
        self.weight = 10

    def speak(self):
        print('woof')

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.weight = 4

    def speak(self):
        print('meow')

class Bird(Animal):
    def __init__(self, name):
        super(Bird, self).__init__(name)
        self.weight = 0.5

    def speak(self):
        print('pweeee')

class Fish(Animal):
    def __init__(self, name):
        super(Fish, self).__init__(name)
        self.weight = 0.2

animal = Animal('animal')
animal.speak()
print(animal.weight)
#
dog = Dog('dog')
dog.speak()
print(dog.weight)
#
cat = Cat('cat')
cat.speak()
print(cat.weight)
#
bird = Bird('bird')
bird.speak()
print(bird.weight)
#
fish = Fish('fish')
fish.speak()
print(fish.weight)

#----------

class seven_A:
    def __init__(self, name):
        self.name = name
        self.gpa = 0

    def character(self):
        pass

class Kira(seven_A):
    def __init__(self, name):
        super(Kira, self). __init__(name)
        self.gpa = 4.8

    def character(self):
        print('reader')

class Diane(seven_A):
    def __init__(self, name):
        super(Diane, self).__init__(name)
        self.gpa = 4

    def character(self):
        print('painter')

class Helen(seven_A):
    def __init__(self, name):
        super(Helen, self).__init__(name)
        self.gpa = 3.5

    def character(self):
        print('beauty')

class Gleb(seven_A):
    def __init__(self, name):
        super(Gleb, self).__init__(name)
        self.gpa = 0

    def character(self):
        print('left')


seven_A = seven_A('7 A')
seven_A.character()
print(seven_A.gpa)

kira = Kira('kira')
kira.character()
print(kira.gpa)
print(kira.name)

diane = Diane('diane')
diane.character()
print(diane.gpa)
print(diane.name)

helen = Helen('helen')
helen.character()
print(helen.gpa)
print(helen.name)

gleb = Gleb('gleb')
gleb.character()
print(gleb.gpa)
print(gleb.name)



class Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        print(f'cat {self.name} is being initialized and says Meow')

    def say_meow(self):
        print(f'{self.name} says Meow!')

    def print_name(self):
        print("This is", self.name)

    def print_age(self):
         print(f'{self.name} is {self.age} years old')

    def print_weight(self):
        print(f"{self.name}' s weight is {self.weight}")

    def eat(self, food):
        print(f'{self.name} ate {food}')


black_cat = Cat('Tom', 2, 8)
black_cat.print_name()
black_cat.print_age()
black_cat.print_weight()
black_cat.eat('fish')


grey_cat = Cat('Luky', 3, 14)
print(grey_cat)
grey_cat.print_name()
grey_cat.print_age()
grey_cat.print_weight()

#----------

class Person:
    def __init__(self, name, dob, height, gender):
        self._name = name #_ чтобы нельзя было поменять данные
        self.__dob = dob # __чтобы нельзя было поменять данные
        self.height = height
        self.gender = gender

    def get_name(self):
        return self._name
person_one = Person('John', 'may 1, 2000', 6, 'M')
print(person_one.get_name())

#----------

class Draw:
    color = 'red'
    form = 'circle'
    def changecolor(self,newcolor):
        self.color = newcolor
    def changeform(self,newform):
        self.form = newform
object1 = Draw()
object2 = Draw()

print(object1.color, object1.form)
print(object2.color, object2.form)

object1.changecolor('green')
object2.changecolor('blue')
object2.changeform('oval')

print(object1.color, object1.form)
print(object2.color, object2.form)

#----------

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    @staticmethod
    def displayCount():
        print('Total employee %d' % Employee.empCount)

    def displayEmployee(self):
        print('Name : ', self.name, ", Salary: ", self.salary)

emp1 = Employee('Zara', 2000)
emp2 = Employee('Manny', 5000)

emp1.displayEmployee()
emp2.displayEmployee()
Employee.displayCount()

#----------

class Computer:
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model
lenovo = Laptop('Lenovo', 2, 512, 'l420')

print('This computer is:', lenovo.computer)
print('This computer has ram of:', lenovo.ram)
print('This computer has ssd of:', lenovo.ssd)
print('This computer has this model:', lenovo.model)

#----------

class Alive:
    eat = 'eat'
    breath = 'breath'
    reproduce = 'reproduce'

    def changeAnimal(self, neweat, newbreath, newreproduce):
        self.eat = neweat
        self.breath = newbreath
        self.reproduce = newreproduce

tiger = Alive()

tiger.changeAnimal('meat', 'lungs', 'mammal')
print(tiger.eat, tiger.breath, tiger.reproduce)

#----------

class Mac:
    director = 'Director'
    def __init__(self, name, salary, worktype):
        self.name = name
        self.salary = salary
        self.worktype = worktype
    def print_workers(self):
        print(f'Director name is: {Mac.director} \n', '\nWorker name is: ', self.name, "\nWorker salary is: ", self.salary, "\nWorker worktype is: ", self.worktype)
class PA(Mac):
    def __init__(self, name, salary, worktype):
        super().__init__(name, salary, worktype)

class CA(Mac):
    def __init__(self, name, salary, worktype):
        super().__init__(name, salary * 1.2, worktype)
worker1 = PA('Peter', 1000, "parttime")
worker2 = CA('Grace', 1000, "fulltime")

worker1.print_workers()
worker2.print_workers()

#----------

