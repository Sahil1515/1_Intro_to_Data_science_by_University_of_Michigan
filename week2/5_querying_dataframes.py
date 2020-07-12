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
print(df.columns)

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

bool_array_with_summer_golds=df['Gold']>0
print(bool_array_with_summer_golds.head(15))







# # now we will overlay this boolean file over dataframe to get only those countries which got gold >0 in Summer
# #For this we use: where as an dot function of the csv file container

# only_gold=df.where(bool_array_with_summer_golds)
# # or:only_gold=df.where(df['Gold']>0 )
# print(only_gold.head(15))

# # print(df.count())
# print("\n\nTo check tje effect of the above function we are checking the length of old and new data\n")
# print("Old data length: {}".format(df['Gold'].count()))
# print("New data length: {}".format(only_gold['Gold'].count()))

# # Now we will drop those rows which have the nan data or no data
# print("Now we will drop those rows which have the nan data or no data")
# only_gold=only_gold.dropna().........................................................>>>>>...>>>>>
# print(only_gold.head(10))
# print(len(only_gold))





# Instead of all the above lines of the paragraph we could simply do it 
#without using the where clause
only_gold=df[df['Gold']>0]
print(only_gold.head(10))

# Gold in winter or in Summer
print("Gold in winter or in Summer: {}".format(len(df[(df['Gold']>0) | (df['Gold.1']>0)])))

print("Gold in winter and not in summer: {}".format(len(df[(df['Gold']==0) & (df['Gold.1']>0)])))
print(df[(df['Gold']==0) & (df['Gold.1']>0)])

print(df.iloc[2])

print("\n\n")
print(df.head(60))
print(df["Gold"])
# print(df.T['Afghanistan (AFG)']): Not working so how to access the row







