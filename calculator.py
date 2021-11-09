num1= int(input("enter the 1st number"))
num2=int(input("enter the 2nd number"))
choice=int(input("please select the number between 1-4"))
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

if choice==1:
    print(num1, 1, num2,"=", add(num1,num2))
elif choice==2:
    print(num1,2,num2,"=",num1-num2)
elif choice==3:
    print(num1,3,num2,"=",num1*num2)
elif choice==4:
    print(num1,4,num2,"=",num1/num2)

else:
    print("enter valid number from 1 to 4")



