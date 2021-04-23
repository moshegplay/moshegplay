print("now will calculate your marketing:\nprices:\n------------\ntomato=3 NIS\ncucamber=2 NIS\ncola=5 NIS\nchicken=20 NIS\n ")
ntomatos=int(input("enter how many ntomatos?\n"))
ncucambers=int(input("enter how many ncucambers?\n"))
colas=int(input("enter how many colas?\n"))
nchickens=int(input("enter how many nchickens?\n"))

print("\nsummary of your order:\n----------\ntomatos: " +str(ntomatos) + "\ncucambers: " +str(ncucambers) + "\ncolas: " +str(colas) + "\nchickens: " + str(nchickens))


summary=(ntomatos*3)+(ncucambers*2)+(colas*5)+(nchickens*20)
print("\nyou have to pay: " + str(summary) + " NIS whitout tax")
print("\nyou have to pay: " + str("%.2f" % (summary*1.17)) + " NIS whit tax")
