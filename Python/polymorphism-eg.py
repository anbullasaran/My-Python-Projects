
#Polymorphism means “many forms”.
#In Python, it allows us to use the same method name but the behavior changes based on the object.

class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

# Function that shows polymorphism
def animal_sound(animal):
    print(animal.make_sound())


# Using different objects
dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)   # Woof!
animal_sound(cat)   # Meow!
animal_sound(cow)   # Moo!

# another example   
class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,grade):   
        self.grade=grade
        super().__init__(name)  # calling parent class constructor
    def display(self):
        print("Name:", self.name)
        print("Grade:", self.grade)

stdObj=student("Saranya","A")
stdObj.display()
        
# another example

class vehicle:
    def start(self):
        return "Vehicle is starting"
class car(vehicle):
    def start(self):
        return "Car is starting with a roar!"
class bike(vehicle):
    def start(self):
        return "Bike is starting with a vroom!"

def vehicle_start(v):
    print(v.start())

v1=vehicle()
c1=car()
b1=bike()   
vehicle_start(v1)  # Vehicle is starting
vehicle_start(c1)  # Car is starting with a roar!
vehicle_start(b1)  # Bike is starting with a vroom!

# another example
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,department):
        self.department=department
        super().__init__(name,salary)  # calling parent class constructor
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

mgrObj=manager("Saranya",50000,"IT")
mgrObj.display()    