import random

listOfNames = input("Enter all the names : ").split(",")
# takes a string as input and then puts it in an array after spliting using a char

print(f"The bill must be paid by {listOfNames[random.randint(0,len(listOfNames)-1)]}")
