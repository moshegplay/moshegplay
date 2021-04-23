from random import randint
'''
fibo=[1,2,3,5,8,13,21]

boolean="True"
#for i in range(2,7):
for i in range(2,len(fibo)):
    print(fibo[i])
    print(fibo[i-1])
    print(fibo[i-2])
    print("\n")
    if fibo[i]==(fibo[i-1]+fibo[i-2]):
        continue
    else:
        boolean="false"
        break

if boolean=="true":
    print("It is fibo series")
else:
    print("It isn't fibo series")
'''

'''
fibo=[1,2,3,5,8,13,21]

boolean="True"
#for i in range(2,7):
for i in range(2,len(fibo)):
    print(fibo[i])
    print(fibo[i-1])
    print(fibo[i-2])
    print("\n")
    if fibo[i]!=(fibo[i-1]+fibo[i-2]):
        boolean="false"
        break

if boolean=="true":
    print("It is fibo series")
else:
    print("It isn't fibo series")
'''


counter=0
while(True):
    choice=input("Menu: \n-----------\n1.printing 100 numbers\n2.check fibo\n3.randint numbers until we get 12 we count 10 times\n")
    if (choice == "1"):
        for i in range(1, 101):
            print(i)
    elif (choice == "2"):
        # fibo [1,2,3,5,8,13,21]
        fibo = []
        for i in range(7):
            fibo.append(int(input("Enter a number: ")))
        boolean = "True"
        for i in range(2, len(fibo)):
            print(fibo[i])
            print(fibo[i - 1])
            print(fibo[i - 2])
            print("\n")
            if fibo[i] != (fibo[i - 1] + fibo[i - 2]):
                boolean = "false"
                break
        if boolean == "True":
            print("It is fibo series")
        else:
            print("It isn't fibo series")
    elif (choice == "3"):
        num=randint(1,12 or counter<10)
        while (num!=12 and counter<11):
            print("counter: " + str(counter)+" Number: " + str(num)+ "\n")
            counter=counter+1
            num=randint(1,12)
    else:
        print("Enter1-3 only!\n")
        continue
    exit = input("Do you want exit? y/n\n")
    if exit != "y":
        continue
    print("Tank you and bye bye...\n")
    break
