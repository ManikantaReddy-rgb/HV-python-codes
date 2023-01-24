total=0       #This is a global variable
def Sum(para1,para2):
    total=para1+para2  #this is a local variable
    print("the total is",total)
    return total
Sum(10,20)
print("The new total is:",total)
