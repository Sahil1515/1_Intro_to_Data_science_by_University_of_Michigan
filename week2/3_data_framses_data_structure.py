import pandas as pd
import numpy as np

print("Creating the data frames")
sports1={
    "Athletics":"Sahil1",
    "Football":"Ishan1",
    "Tenis":"Annanya1"
}
sports2={
    "Athletics":"Sahil2",
    "Football":"Ishan2",
    "Tenis":"Annanya2"
}
sports3={
    "Athletics":"Sahil3",
    "Football":"Ishan3",
    "Tenis":"Annanya3"
}
df=pd.DataFrame([sports1,sports2,sports3],index=["team1","team2","team3"])
print(df)

print("\n\nNow operations on the data frame cretaed above")
print("Using ilco")
print(df.iloc[2]) 
print("\nTeam 1")
print("Using loc")
print(df.loc["team1"])

print("Accessing the single box of data")
print(df.loc["team2","Athletics"])
print(df.loc["team1",["Athletics","Football","Tenis"]])

#or we can access the data as:
#but try to avoid this as this gives the copy of the data frame instead of the view on the dataframe
print(df.loc["team1"]["Tenis"])

# Getting the transpose of the data frame
print("Getting the transpose of the data frame")
print(df.T)

#Slicing with the loc or iloc 
print("Slicing with the loc or iloc")
print()
print(df.loc[:])
print()
print(df.loc[:,["Athletics","Football"]])

# Dropinng/Deleting  the data:
print()
print("Drop using: drop()")
#This dosen't delete from the original dataframe but creates the new copy
#drop takes two optional parameters : 
    #inplace: if set to true deletes inlpace else creates the copy
    #axex: if set to 0 means the row and if set to 1 means the column
df_new=df.drop('team1')
print(df_new)
print("\nCheck after the drop command when inplace is default to false")
print(df)

print("\nDeleting inpalce by setting the inplace parameter to true")
df.drop('team1',inplace=True)
print(df)
df.drop("Football",inplace=True,axis=1)
print(df)
print()

#This deletes from the original dataframe permanantly
print()
print("This deletes only the keys: i.e only along the columns and not the particular row. So do that by drop function only")
print("Drop using: del keyword")
del df["Tenis"]
print(df)

