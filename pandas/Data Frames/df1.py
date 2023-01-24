#Data frame is an multi dimensional Array
import pandas as pd
Entries={
    "Temperature":[99,100,102,98,80],
    "Days":["mon","tue","wed","thu","Fri"]
}
df=pd.DataFrame(Entries)
print(df)
# print(df.loc[3])