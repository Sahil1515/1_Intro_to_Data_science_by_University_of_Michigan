import numpy as np
import pandas as pd

print("QUERYING A SERIES")
sports={
    "Athletics":"Sahil",
    "Football":"Ishan",
    "Tenis":"Annanya"
}
s=pd.Series(sports)
print(s)

print(""" iloc and loc
 iloc means by index location i.e 0,1,2,3,4,5 and so on
 loc means the location of the provided item in the loc attribute""")
print(s.iloc[0])
print(s.loc["Athletics"])
#Comment
print('''WE can do it eithout the use of the loc and iloc also
 but if it was  an integer series only then it will create the confusion.
  So it's always better to use the loc and iloc attributes\n''')
print(s[0])
print(s["Athletics"])
#Example to explain above
print("Exampe to explain above")
d={99:"Sahil",
   100:"Saini",
   101:"Salaria"
    }
sr=pd.Series(d)
print(sr)
# print(sr[0]): this will create an error
#So we use 
print(sr.iloc[0])


#Working with the data of the series
print("Working with the data of the series")
float_series=pd.Series([1.2,2.3,4.5,2.1])
print(float_series)

print("Numpy and Pandas support the vactorization")
#Sum: its faster than the older approch of going through each value of the series using the loop
print("Sum")
sum=np.sum(float_series)
print(sum)

print("Other way")
sum_2=0
for item in float_series:
    sum_2+=item
    print(item)
print("Sum of the float array : {}".format(sum_2))


#Creating big series
print("Creating big series")

#np.random.randint(sratting_point, in_between, end_point)
big_series=pd.Series(np.random.randint(0,1000,10000))
print("Head prints only first five elements")
print(big_series.head())
print("Length of serie: {}".format(len(big_series)))

#broadcasting: changing? modifying each value of the list
print("Changing each value of big_series by 2")
big_series+=2
print(big_series.head())

#Real way i.e bruteforce 
print("Very very important please see the code properly")
#here big_series.iteritems() is required because we wanna iterate through both the value as well as theindex.
# Else we could traverse simply as in the array
for label,value in big_series.iteritems():
    big_series._set_value(label,value+2)
print(big_series.head())

#Another approch
print("Another approch")
big_series=pd.Series(np.random.randint(0,1000,10000))
print(big_series.head())
for label,value in big_series.iteritems():
    big_series.loc[label]=value+2
print("After modifying by +2")
print(big_series.head())

# mix value allowed 
print("mix value allowed  ")
print(float_series) 
float_series.loc[4]="Animal"# Not iloc because it will go and search for index 4. which is not present so throws an error
print(float_series)