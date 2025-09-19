
'''def samPgm(x):
    a=0
    for i in range(1, x + 1):
        a = a+ i  
    print("Sum of first five natural numbers :",a)
samPgm(5)'''

'''a=[]
for i in range(5):
    num=int(input("Enter the number " + str(i+1) + ":-"))
    a.append(num)
print(a)'''

# Dont use range in for loop if wants use array with the elements (values)
a=[12,25,30,45,50]
for i in a:
    if i%2==0:
        print(i,"is even number")
    else:
        print(i,"is odd number")
