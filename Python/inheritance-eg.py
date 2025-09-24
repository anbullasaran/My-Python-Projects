
#multiple inheritance

'''
class dad:
    def phone(self):
        print("I have a phone") 
class mom:
    def car(self):
        print("I have a car")   
class child(dad,mom): # Inheriting from dad and mom class
    def bike(self):
        print("I have a bike")  


dadObj = dad()
momObj = mom()
childObj = child()
childObj.phone()   
childObj.car() 
childObj.bike() '''

#multilevel inheritance

'''class grandpa:
    def money(self):
        print("I have money")
class father(grandpa):
    def phone(self):
        print("I have a phone") 
class son(father):
    def bike(self):
        print("I have a bike")  

sonObj = son()
sonObj.money()   
sonObj.phone() 
sonObj.bike()'''

#hierarchical inheritance

'''
# Parent class
class Animal:
    def animalTypes(self):
        print("There are lots of animals")

# Child class 1
class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

# Child class 2
class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

# Child class 3
class Cow(Animal):
    def speak(self):
        print("Cow says: Moo!")

# Create objects of each child class
dog = Dog()
cat = Cat()
cow = Cow()
animalObj = Animal()

animalObj.animalTypes()  # Animals can make sounds
#animalObj.speak()  # Error will occur as parent class cannot access child class methods
dog.animalTypes()  # Animals can make sounds
dog.speak()  # Dog says: Woof!
cat.speak()  # Cat says: Meow!
cow.speak()  # Cow says: Moo!

'''

#Hybrid inheritance

#Hybrid inheritance = combination of two or more types of inheritance.

# Parent class
class Person:
    def show(self):
        print("I am a person")

# Child class 1 (Single Inheritance)
class Student(Person):
    def show_student(self):
        print("I am a student")

# Child class 2 (Hierarchical Inheritance)
class Teacher(Person):
    def show_teacher(self):
        print("I am a teacher")

# Child class 3 (Multiple Inheritance)
class TeachingAssistant(Student, Teacher):
    def show_ta(self):
        print("I am a teaching assistant")
        

# Create objects
s = Student()
t = Teacher()
ta = TeachingAssistant()

s.show()          # From Person
s.show_student()

t.show()          # From Person
t.show_teacher()

ta.show()         # From Person (inherited via Student/Teacher)
ta.show_student() # From Student
ta.show_teacher() # From Teacher
ta.show_ta()      # Own method