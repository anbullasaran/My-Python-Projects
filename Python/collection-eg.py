# Collections (Arrays in python) examples 
'''
1. List
2.Tuple
3.Set
4.Dictionary
'''

# List example - ordered(can access with index), Changable, allows duplicate elements
a=[10,20,30,40,50]
print(a)
print(type(a))
print(a[0])
a[0]=100 # update value
print(a)


# Tuple example - ordered(can access with index), unchangable, allows duplicate elements
t=(10,20,30,40,50)
print(t)
print(type(t))
print(t[0])
#print(t[0]=100) # will give error


# Set example - unordered(cannot access with index), changable, no duplicate elements
s={10,20,30,40,50}
print(s)
print(type(s))
#print(s[0]) # will give error
s.add(60) # add new element
print(s)
s.add(20) # will not add duplicate element
print(s)

# Dictionary example - unordered(Can access with Key-value pair), changable, yes for value & no for keys- duplicate elements    
d={1:"Saranya",2:"Saathvikan",3:"Saanvi",4:"Suresh"}
print(d)
print(type(d))
print(d[1]) # access with key value
print(d.get(2)) # access with key value
d[5]="Sathya" # add new key value pair
print(d)
d[2]="Saathvik" # update existing key value pair
print(d)