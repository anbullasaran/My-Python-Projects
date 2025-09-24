#super keyword example

'''
If both parent and child classes have constructors (__init__):
	•	When you create an object of the child class, by default → child class constructor is called(override).
	•	But if the child wants to also run the parent’s constructor, you must explicitly call it using super().__init__().
'''

class A:
    def __init__(self):
        print("This is constructor of class A")
    def display(self):
        print("This is class A")                
class B(A):
    def __init__(self):
        print("This is constructor of class B")
        super().__init__()  # calling parent class constructor
    def display(self):
        print("This is class B")
        super().display()  # calling parent class method using super keyword
class C(B):
    def __init__(self):
        print("This is constructor of class C")
        super().__init__()  # calling parent class constructor
    def display(self):
        print("This is class C")
        super().display()  # calling parent class method using super keyword   
         
obj = C()
obj.display()
