import pandas as pd
import numpy as np

animals=["Tiger","Bear","Moose"]
animal_series=pd.Series(animals)
print(animal_series)
numbers=[1,2,3,4,5,6]
num_series=pd.Series(numbers)
print(num_series)

#HANDLING MISSING DATA
animals=["Tiger","Bear",None]
animal_series=pd.Series(animals)
print(animal_series)

#NAN >>>>>>>>first converts automatically every int to float and then none to nan
numbers=[1,2,3,4,5,None]
num_series=pd.Series(numbers)
print(num_series)
# nan speciallity
print("nan speciallity")
print(np.nan==None)
print(np.nan==np.nan)
#Proper operation using np.isnan()
print(np.isnan(np.nan))

#Series is like in between product of the series and the dictionary
# Create series using the dictionary
#Here all the keys become the indiceies and not 0's and 1's
print("Create series using the dictionary")

sports={
    "Athletics":"Sahil",
    "Football":"Ishan",
    "Tenis":"Annanya"
}
print("Printing the sports dictionary")
sp=pd.Series(sports)
print(sp)


#Above all the keys become the indiceies and not 0's and 1's
#Or we can do it by setting the indicies explicitly
print('by setting the indicies explicitly')
s=pd.Series(animals,index=[0,1,2]) # if i give the dictionary here it will not work as expected
print(s)

