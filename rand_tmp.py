from random import randint
from time import sleep

print("getting random numbers...")
sleep(3)
num1=randint(1,37)
num2=randint(1,37)
print("\n1st number: "+str(num1) + "\n2nd number: " +str(num2)+"\n")
if (num1==num2):
    print("you won 100$ \n")
else:
    print("you won 0$ \n")
print("bye bye...\n")
