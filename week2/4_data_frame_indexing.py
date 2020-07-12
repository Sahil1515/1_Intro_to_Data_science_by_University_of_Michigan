import pandas as pd
import numpy as np

list_1=[1,2,3,4,5]
list_2=[1.1,2.2,3.3,4.4,5.5]
df=pd.DataFrame([list_1,list_2],index=['list_1','list_2'])
print(df)
df=df.T
print(df)
list_1_copy=df.loc[:,"list_1"]
print(list_1_copy)
list_1_copy+=list_1_copy
print(df)

df=pd.read_csv('C:/Users/Sahil/Desktop/data_scdience_practice/UM_DataSciWithPython_1/olympics.csv')
print(df.head())

# modifying 
print()
df=pd.read_csv('C:/Users/Sahil/Desktop/data_scdience_practice/UM_DataSciWithPython_1/olympics.csv',index_col=0,skiprows=1) 
# df=pd.read_csv('C:/Users/Sahil/Downloads/olympics.csv',index_col=0,skiprows=[1,2,3,4])
# this will remove the avobe mentioned rows in the list 
print(df.head())

# Editting the csv file directily  
print("\n\n")
print("Editting the csv file directily")
print(df.columns)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]},inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]},inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]},inplace=True)
print(df.head())
