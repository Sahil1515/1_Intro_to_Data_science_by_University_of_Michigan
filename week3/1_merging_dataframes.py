import pandas as pd
import numpy as np

staff_df=pd.DataFrame([
    {'Name':'Kelly', 'Role':'Director of HR'},
    {'Name':'Sally', 'Role':'Course liaison'},
    {'Name':'James', 'Role':'Gardner'}
  ])
staff_df=staff_df.set_index('Name')
print(staff_df)
print()
student_df=pd.DataFrame([
    {'Name':'James', 'School':'Business'},
    {'Name':'Mike', 'School':'Law'},
    {'Name':'Sally', 'School':'Engineering'}
  ])
student_df=student_df.set_index('Name')
print(student_df)

# Inner Join
print('\n\nInner Join')
print(pd.merge(staff_df,student_df, how ='inner',left_index=True, right_index=True))

print('\n\nFull Outer Join')
print(pd.merge(staff_df,student_df, how ='outer',left_index=True, right_index=True))

print('\n\nLeft Outer Join')
print(pd.merge(staff_df,student_df, how ='left',left_index=True, right_index=True))

print('\n\nRight Outer Join')
print(pd.merge(staff_df,student_df, how ='right',left_index=True, right_index=True))



# We can also do it without the use of index usnig yhe left_on and right_on set to True
print("\n\nWithout indicies  ")
staff_df=staff_df.reset_index()
student_df=student_df.reset_index()
print(pd.merge(staff_df,student_df,how='inner',left_on='Name',right_on='Name'))

#Note:: if the indices overlap like names. Or create confusion then we can pass a list in left_on or right_on
