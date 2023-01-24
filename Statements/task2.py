num = [int(input("Enter Five students marks:")) for _ in range(5)]
for i in num:
    if(i<=40):
        continue
    print("The students marks are:",i)
