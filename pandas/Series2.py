import pandas as pd
Calories ={"Day1":450,"Day2":420,"Day3":460,"Day4":550,"Day5":660}
Check=pd.Series(Calories, index=["Day1","Day5"])
print(Check)