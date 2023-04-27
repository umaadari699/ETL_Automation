from io import StringIO

import numpy as np
import pandas as pd
import datacompy
from attr.filters import include

df1 = pd.read_csv(r'C:\Users\uma.adari\Downloads\Emp_Table.csv')
df2 = pd.read_csv(r'C:\Users\uma.adari\Downloads\Results.csv')
print('Mismatch',df2[~df2.isin(df1.to_dict('1')).all(1)].to_string())
# In High level,Check Both are Same or Now
print(df1.equals(df2)) # O/p gives true or false
print("Intersect Col",df1.columns.intersection(df2.columns)) # Matched column names will return
print("Differ Col DF1",df1.columns.difference(df2.columns))# Return which present in DF1 and not Present in df2
print("Diff Col DF2",df2.columns.difference(df1.columns))# Return which present in DF2 and not Present in df1
print(df2.select_dtypes(include=['float','int'])) # Retrun DATA of Specific datatype
print(df2.select_dtypes(include=['float','int']).columns) # Return Column names only
#Example for Renaming new column names
#df.columns = ['name', 'physics', 'biology', 'geometry', 'calculus']

# column= list(df2.select_dtypes(include=['float']))
# #print((df2[column].astype(str).round(decimals=3)))
# df2[column]=df2[column].fillna('0').astype(int).round(decimals=2)
#
# ht_re=df2.to_html()
# file_l=open("Index.html",'w')
# file_l.write(ht_re)





# with pd.ExcelWriter("diff.xlsx", mode='w') as writer:
#     df3.to_excel(writer, sheet_name='outer', index=False)
#     print(df3.to_string())



