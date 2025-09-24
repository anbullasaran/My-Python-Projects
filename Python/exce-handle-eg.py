# exception Handling example
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
finally:
    print("Execution completed.")   



# another example

'''
value error
type error
name error
index error
key error
attribute error
io error
zero division error
'''

try:
    a = [1, 2, 3]
    print(a[3])  # This will raise an IndexError
except IndexError as e:
    print("Index Error occurred:", str(e))
except ValueError as e:
    print("Value Error occurred:", str(e))
except TypeError as e:  
    print("Type Error occurred:", str(e))
except NameError as e:
    print("Name Error occurred:", str(e))
except Exception as e:
    print("An unexpected error occurred:", str(e))
finally:
    print("Execution completed.")

    # File handling example

    f=open("testfile.txt","w")
    #print(f.name)
    print(f)
    f.write("This is a test file.")
    f.close()  # impartant for write operation

    f1=open("testfile.txt","r")
    print(f1)
    f1.read()
    f1.close()

    f2=open("testfile.txt","r+") # read and write operation
    print(f2)
    f2.read()
    f2.write(" This is added text.")
    f2.close()

    f3=open("testfile1.txt","a") # append operation -add the data to existing file
    print(f3)
    f3.readline() # read the first line from file   
    f3.write(" This is appended text.")
    f3.close()
