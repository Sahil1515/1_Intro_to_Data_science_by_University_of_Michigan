import numpy as np 
import pandas as pd 
# np.random.binomial(n,p,size=Number of times)--> n from 0 to n
print(np.random.binomial(1,0.5,10))#nCr
x=np.random.binomial(100,0.5)/100
print(x)

# Q
x=np.random.binomial(20,0.5,1000)
print((x>=15).mean())

# TO check if two days had tornado daily
prob_of_tornado=0.01

dist_of_tornado=np.random.binomial(1,prob_of_tornado,1000000)

two_days_in_row=0
for j in range(1,len(dist_of_tornado)-1):
    if dist_of_tornado[j]==1 and dist_of_tornado[j-1]==1:
        two_days_in_row+=1

print("{} back to back tornados occur in {} years".format(two_days_in_row,1000000/365))