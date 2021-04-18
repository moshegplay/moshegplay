#lists
'''
new_list=[]
new_list2=list()
print(type(new_list))
print(type(new_list2))
'''

'''
new_list=[2,6.6,"idan hakimi",[]]
print(type(new_list))
print(new_list)
new_list2=new_list+[77,'hello world']
print(new_list2)
new_list3=new_list2*3
print(new_list3)
'''

'''
my_list=[1,2,28,6.6,"dudu cohen"]
print("my age: " + str(my_list[2]))
'''

'''
my_list2=list("1234567")
print(my_list2)

my_string=''.join(my_list2)
print(my_string)

my_list3=my_string.split()
print(my_list3)
'''

'''
my_string="hello idan \nhow are you?"
my_list=my_string.splitlines()
print(my_list)
'''

'''
my_list=["hello",1,6.6,"idan",55,77.7]
print("the lenth is: " + str(len(my_list)))


my_str="0123456789"
print("the lenth is: " + str(len(my_str)))
'''

'''
my_list=["hello",1,6.6,"idan",55,77.7]
print("the lenth is: " + str(len(my_list)))

my_list.append("wow")
my_list.append("idan")
print(my_list)
print("the new lenth is: " + str(len(my_list)))

my_list.insert(7,"dudu")
print(my_list)

my_list.pop(7)
print(my_list)
'''

my_list=["googel","facebook","ebay","apple"]
print("net4u" in my_list)
