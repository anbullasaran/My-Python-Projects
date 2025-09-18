
'''def samPgm(x):
    a=0
    for i in range(1, x + 1):
        a = a+ i  
    print("Sum of first five natural numbers :",a)
samPgm(5)'''

a=[]
for i in range(5):
    num=int(input("Enter the number " + str(i+1) + ":-"))
    a.append(num)
print(a)