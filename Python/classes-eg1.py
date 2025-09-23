class student:
    def __init__(self):
        self.name = "saranya"
        self.age = 39

    def display(self):
        #print("Name:", self.name)
        #print("Age:", self.age)
        return self.name, self.age
    
s1 = student()
s2= student()

s1.display()

s2.name="vinayaka"
s2.age="100"

s2.display()
#print(s1.display())
print("Name:", s1.name)
print("Age:", s1.age)
print("Name:", s2.name)
print("Age:", s2.age)