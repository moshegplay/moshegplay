##for loops
from time import sleep

'''
for x in range(1,11):
    print(x)
    print("wow\n")
'''

'''
list_idan=["banana","appel" ,"mango"]
for x in list_idan:
    print(x)
'''
'''
list_idan=["banana","appel" ,"mango"]
print(len(list_idan))
for x in range(len(list_idan)):
    print(list_idan[x])
'''

'''
for x in range(1,11,3):
    print(x)
    print("wow\n")
'''

print("Now we will get all the details about your class: \n-------------------------------------------------\n")
for i in range(4):
    name=input("Enter a Name:  ")
    age=int(input("Enter an Age: "))
    phone=int(input("Enter a Phone: "))
    print("printing student number " +str(i+1) + " details...\n" )
    sleep (3)
    print("Full name: " + name + "\nAge: " +str(age) + "\nPhone:" +str(phone) + "\n---------------\n")

print("\nBye Bey... ")

