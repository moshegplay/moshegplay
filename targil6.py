'''
NAME=input("Enter a name: ")
if(NAME=="idan"):
    print("hello Idan\n")
    AGE = int(input("Enter your age: "))
    if (AGE == 28):
        print("wow you are 28 years old")
    else:
        print("you are too yuong")
else:
    print("where is Idan?\n")
'''

'''
"enter a number: \n"
number=int(input("enter a number: \n"))
if(number<=6):
     print(number*2)
else:
    print(number-1)
'''

name=input("Enter your name: \n")
age=int(input("Enter your age: \n"))
if((name=="idan" or name=="Idan")and(age>=18)):
    print("you can enter to the club!")
else:
    print("you are not allowed to enter...")
