'''def numbersList(x):
    a=[]
    for i in range(x):
        num=int(input("Enter the number " + str(i+1) + ":-"))
        a.append(num)
    #print(a)
    #find the even and odd numbers in the list
    even=[]
    odd=[]
    for j in a:
        if j%2==0:
            even.append(j)
        else:
            odd.append(j)
    print("Even numbers in the list are :",even)
    print("Odd numbers in the list are :",odd)
        
        
numbersList(5)
'''

#using return statement
def numbersList(x):
    a=[]
    for i in range(x):
        num=int(input("Enter the number " + str(i+1) + ":-"))
        a.append(num)
    #print(a)
    #find the even and odd numbers in the list
    even=[]
    odd=[]
    for j in a:
        if j%2==0:
            even.append(j)
    for k in a:
        if k%2!=0:
            odd.append(k)
       
    return "Even MNumbers",even,"odd numbers",odd
   # return odd
    #print("Even numbers in the list are :",even)
    #print("Odd numbers in the list are :",odd)
        
        
numListE = numbersList(5)
#numListA = numbersList(5)
print(numListE)
#print(numListA)
