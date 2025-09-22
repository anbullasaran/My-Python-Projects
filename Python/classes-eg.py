class India:
    def __init__(self):
        print("This is constructor")
        self.name=""
        self.capName=""
    def places(self): # self refers to the current object
        #print ("First eg for class & functions")
        print("place object name is :",self.name)
        print("place object Capital name is :",self.capName)  #object.variableName = self.variableName
        #return 
    def captial(self):
        print("place object name is :",self.name)
        print("place object Capital name is :",self.capName)
        #return
        #print("Capital of India is New Delhi")

placeObj1 = India() #obj1
captObj2 = India() #obj2

placeObj1.name = "Chennai"
placeObj1.capName = "Washington DC"
captObj2.name = "Trichy"
captObj2.capName = "Delhi"

placeObj1.places()
placeObj1.captial()

captObj2.places()
captObj2.captial()

'''print("City name is :",placeObj1.name)
print("captial is :",placeObj1.capName)
print("City name is :",captObj2.name)
print("captial is :",captObj2.capName)'''

    