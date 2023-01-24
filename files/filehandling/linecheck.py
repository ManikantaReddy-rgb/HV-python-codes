check = input("Enter the file name: ")
num_lines = 0
with open(check,'r') as x:
    for line in x:
        num_lines+=1

print("Number of lines",num_lines)