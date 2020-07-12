import pandas as pd
import numpy as np

print("Split. Apply. Combine\n\n")

df=pd.read_csv('C:/Users/Sahil/Desktop/data_scdience_practice/UM_DataSciWithPython_1/census.csv')
df=df[df['SUMLEV']==50]
print("\n\n")
g=df.groupby('STNAME')
# for STNAME,city_df in g:
#     print(STNAME)
#     print(city_df)

#To get some particular group
print('\n\nTo get some particular group')
print(g.get_group('Alaska'))
#Mean/Average
print("\n\nMean")
print(g.mean())

#Max
print("\n\nMax")
print(g.max())

#Min
print("\n\nMin")
print(g.min())

#Describe   
# print("\n\nDescribe")
# print(g.describe())
#because this takes a long

print("\n\n")
print("\n\nMAX")
print(g['CENSUS2010POP'].mean())


# Coursera
print("Coursera")

df=df.set_index('STNAME')

def fun(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

for group , frame in df.groupby(fun):
    print("the group "+str(group)+ " has records "+str(len(frame)))


#Mean
print("\n\nMean")
df=pd.read_csv('C:/Users/Sahil/Desktop/data_scdience_practice/UM_DataSciWithPython_1/census.csv')
df=df[df['SUMLEV']==50]
# g=df.groupby('STNAME').agg(('CENSUS2010POP':np.average))
# print(g)
print("\n\ng=df.groupby('STNAME').agg(('CENSUS2010POP':np.average))")
func=['mean','sum','max','count']
print(df.set_index('STNAME').groupby(level=0)[['CENSUS2010POP']].agg(func))

# If you want to apply different function on different variable
print("\n\nIf you want to apply different function on different variable")
print(df.groupby('STNAME').agg({'REGION':'max','STATE':'min','COUNTY 0  ':'mean'}))
#Count just finds the numbe rof NaN values in a column and not the tota values in a column

print(df['SUMLEV'].count())
print(len(df['SUMLEV']))

#Value_counts()

df=pd.read_csv('C:/Users/Sahil/Desktop/data_scdience_practice/UM_DataSciWithPython_1/census.csv')
print("\n\nvalue_counts()")
print(df['STNAME'].value_counts())

#Percentage
print("Percentage")
print(df['STNAME'].value_counts(normalize=True))