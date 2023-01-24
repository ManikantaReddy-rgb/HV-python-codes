def Rec_fib(n):
    if (n<=1):
        return n
    else:
        return(Rec_fib(n-1) + Rec_fib(n-2))

Entries=int(input("Enter a number:"))
if (Entries<=0):
    print("Invalid Entry")
else:
    print("Fibono series:")
    for i in range(Entries):
        print(Rec_fib(i))