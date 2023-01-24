n=int(input("Enter a number:"))
sum=0
for i in range(n+1):
    sum += i  #sum= sum + i
print(sum)
print(sum/n)
print(f"sum of {n} numbers: {sum}")
print(f"avg of {n} numbers :{sum/n}")
