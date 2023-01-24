import pandas as pd
a=[1,7,2]
myvar=pd.Series(a, index=["x","y","z"])
print(myvar)

a1=[75,80,95,99,80]
y=pd.Series(a1, index=["RAM","REVI","RAJ","Rahul","Manikanta"])
print(y)


studentname=[input("Enter students name:")for _ in range(5)]
marks=[int(input("Enter students marks:"))for _ in range(5)]
z=pd.Series(marks,index=[studentname])
print(z)