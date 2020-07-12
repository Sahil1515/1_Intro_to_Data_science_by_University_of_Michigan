import pandas as pd
import numpy as np 

#Changing the data set
print("Changing the data set")
df=pd.read_csv('C:/Users/Sahil/Desktop/data_scdience_practice/UM_DataSciWithPython_1/census.csv')
# print(df)

#To get the unique values
print(df['SUMLEV'].unique())


print("\n\n")
df_of_sumlev_50=df[df['SUMLEV']==50]
# print(df_of_sumlev_50.head(10))

#Length
# print(len(df[df['SUMLEV']==40])): 51

print("\n\n")
df=df.set_index(['STNAME','CTYNAME']) 

print(df)