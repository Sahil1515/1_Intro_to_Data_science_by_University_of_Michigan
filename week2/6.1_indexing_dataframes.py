import pandas as pd 
import numpy as np

# from file_4::::


# modifying 
print()
df=pd.read_csv('C:/Users/Sahil/Desktop/data_scdience_practice/UM_DataSciWithPython_1/olympics.csv',index_col=0,skiprows=1) 
# df=pd.read_csv('C:/Users/Sahil/Downloads/olympics.csv',index_col=0,skiprows=[1,2,3,4])
# this will remove the avobe mentioned rows in the list 
print(df.head())

# Editting the csv file directily
print("\n\n")
print("Editting the csv file directily")
# print(df.columns)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]},inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]},inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]},inplace=True)
names_ids = df.index.str.split('(') # split the index by '('
df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

print(df.head())

print("\n\n")

#printing the details of India
print("Printing the details of India")
for country in df.index:
    if country[:6]=='Poland':
        ls1= df.loc[country]
    if country[:5]=='India':
        ls2=df.loc[country]
        
df_poland_india=pd.DataFrame([ls1,ls2])
print(df_poland_india)

#Changing the index column by number of gold in Summer 
print("\n\nChanging thr index column")
df["Country"]=df.index
df=df.set_index('Gold')
print(df.head(10))



#Resetting the index: if required because like the Gold row is empty
print("\n\nResetting the index")
df=df.reset_index()
print(df.head(10))
 
