class Person:

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self,name,idnumber)
        
obj = Employee("Raul", 2343423, 15000, "Intern")
obj.display()


class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printname(self):
        print(self.fname, self.lname)  
class student(Person):

    def __init__(self, fname, lname, year):
        self.graduationyear = year
        super().__init__(fname, lname)

obj = student("Mike", "Olsen", 2024)
obj.printname()
print(obj.graduationyear)

from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class human(animal):
    def sound(self):
        print("I can talk")
class cat(animal):
    def sound(self):
        print("Meow")
class dog(animal):
    def sound(self):
        print("I can bark")
class snake(animal):
    def sound(self):
        print("I can hiss")

a = human()
a.sound()
b = cat()
b.sound()
c = dog()
c.sound()
d = snake()
d.sound()