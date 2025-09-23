#constructor assign values example
class teacher:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

t1=teacher("Saranya",39)
t2=teacher("Vinayaka",100)

#t1.display()
#t2.display()

# Types of variables in classes - instance & class variables

class teacher:
    school = "ABC School"  # class variable
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def setprice(self,price):
        self.price=price  # instance variable
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Age:", self.school)
        print("Price:", self.price)

t1=teacher("Saranya",39)
t2=teacher("Vinayaka",100)
t1.setprice(5000)
t2.setprice(10000)
t1.display()
t2.display()

'''
Notes :
variable assign values 
1. Assign/Pass variable values through constructor
2. obj.variablename = value before calling method
3. create method to assign variable value & call that method before calling display method'''