import pandas as pd
df=pd.read_csv("Studentdetails.csv",usecols=["ROLL NO", "NAME","CLASS"])
print(df)
#spc=df[["NAME","CLASS"]]
#print("The column is:")
#print(spc)
#rint(df.head())
#print(df.tail())


