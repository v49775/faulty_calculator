#Exercise 02 -- Faulty calcultor

# Design a calculator which will correctly solve all the problems except the following ones:
#  45 * 3 = 555 , 56 + 9 = 77 , 56/6 = 4
# Your program should take operator and the two numbers as input from the user and then return the result

no1=int(input("Enter Your first no : "))
no2=int(input("Enter your second no : "))
opr=input("Enter the operator you want to calculate : ")

if (opr=="sum"):
    if(no1==56 and no2==9):
        print(77)
    else:
        print("your calculation is : ",no1+no2)
elif (opr=="sub"):
    print("your calculation is : ",no1-no2)
elif (opr=="mul"):
    if (no1 == 45 and no2 ==3):
        print(555)
    else:
        print("your calculation is : ",no1*no2)
elif (opr=="div"):
    if(no1==56 and no2==6):
        print(4)
    else:
        print("your calculation is : ",no1/no2)


