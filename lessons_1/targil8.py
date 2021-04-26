##while  loops
from time import sleep

'''
num=int(input("Enter a number: "))
while(num!=7):
    print(num*100)
    num = int(input("Enter a number: "))
'''

'''
counter=10
while(counter>0):
    print(counter*100)
    print("Idan Hakimi")
    counter=counter-1
'''

while(True):
    choice=input("Menu:\n-----\n1.Insert Number and ** it by 3\n2.Insert 4 IPs to a list and print it\n3.Insert 4 Entries to DNS_dictiionary and print it\n4.Check if a string is polindrom\n Enter Number from menu: \n")
    if(choice=="1"):
        print("The new number is: " +str((int(input("Enter a number: \n"))) **3))
    elif(choice=="2"):
        list_ip=[]
        list_ip.append(input("Enter new IP: \n"))
        list_ip.append(input("Enter new IP: \n"))
        list_ip.append(input("Enter new IP: \n"))
        list_ip.append(input("Enter new IP: \n"))
        print("\nThe new list:\n------------\n" +str(list_ip))
    elif(choice=="3"):
        dns_dict={}
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        print("\nThe new dns_dict:\n-----------------\n" + str(dns_dict))
    elif(choice=="4"):
        word=input("Enter a word: ")
        if (word == word[::-1]):
            print("this is polindrom!")
        else:
            print("this isn't polindrom!")
    else:
        print("Enter 1-4 Only!...\n")
    exit=input("do you want to exit? y/n\n")
    if(exit=="y" or exit=="yes"):
        break
    else:
        print("Welcome back\n")
print("Thank you and bye bye...")
