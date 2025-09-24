# Encapsulation example - by using private variables (access modifier to hide variable or methods from outside the class

class company:
    def __init__(self):
        self.name="Google"          
        self.__ceo="Saranya"    # private variable
    def display(self):
        print("Ceo:", self.__ceo)  # accessing private variable inside class method

c1=company()
c1.name="ABC"
#print(c1.__ceo)  # will give error
c1.display()  # accessing private variable through class method
print(c1.name)  # accessing public variable

# another example
class bank:
    def __init__(self):
        self._ifsc="SBIN0001234"  # private variable
    def display(self):   # getter method to access private variable
        print(self._ifsc)
class customer(bank):
    pass

cust=customer()
cust.display()  # accessing private variable through class method
print(cust._ifsc)  # accessing private variable outside class - not recommended but possible