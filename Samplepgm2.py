from io import StringIO
import pandas as pd
import datacompy
from attr.filters import include

df1 = pd.read_csv(r'C:\Users\uma.adari\Downloads\Emp_Table.csv')
df2 = pd.read_csv(r'C:\Users\uma.adari\Downloads\Results.csv')
s = df2.sort_values(by='SALARY', ascending=False) # Sorting on Salary in Descending Order
u =s['SALARY'].unique() # Unique records in SALARY column
print(s.iloc[0]) # Get First Record in Results/Table
# dups = df2[df2.duplicated()]
# print(dups.to_string())
#src= df1[df1.isnull().any(axis=1)]
#print(src.to_string())
#df2.groupby(['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL']).EMPLOYEE_ID.size()
#print(df2.groupby('DEPARTMENT_ID').EMPLOYEE_ID.size())
#df1["rnk_1"] = df1[['DEPARTMENT_ID','SALARY']]['SALARY'].rank(axis=0,method='dense',ascending=False)
#print(df1.to_string())
# df1["rank"]= df1.groupby(['DEPARTMENT_ID']).SALARY.rank(axis=0,method='dense',ascending=False)
# print(df1.loc[0]) # get First Record in Results/Table
# print(df1.sort_values(by="rnk_1", ascending=True).to_string()) # Ascending Order
# print(sorted(df1.columns))# Sorting Columns
# print(df1.info())# to know columns datatypes
# print(df1.select_dtypes(include=['float','int'])) # identify Specific datatype columns

#Records that are Present b/w Both and Not present[Extra Records] on PK basis
#if you add query, Can ignore existed records in both else Both Existd and Non Existed will come
merged_df = pd.merge(df1,df2,on='EMPLOYEE_ID',how='outer',indicator=True).query('_merge != "both"')
with pd.ExcelWriter("outer.xlsx",mode='w') as writer:
    merged_df.to_excel(writer, sheet_name='outer', index=False)


