import cx_Oracle
import datacompy
import numpy as np
import oracledb
import pandas as pd
import cx_Oracle
import sqlalchemy
from pandas._testing import assert_frame_equal
from sqlalchemy import create_engine

df1 = pd.read_csv(r'C:\Users\uma.adari\Downloads\Emp_Table.csv')
df2 = pd.read_csv(r'C:\Users\uma.adari\Downloads\Results.csv')
print(len(df1))
comp = datacompy.Compare(df1, df2, join_columns=['EMPLOYEE_ID', 'first_name', 'last_name', 'email',
                                                 'phone_number', 'hire_date', 'job_id', 'salary', 'commission_pct',
                                                 'manager_id', 'department_id'])
comp.matches(ignore_extra_columns=False)
rep = comp.report()  # Complete report generates
print(rep)
notInA = comp.df1_unq_rows  # Not present in DF1 frame
notInB = comp.df2_unq_rows  # not Present in DF2 frame
# Mismatched records values for matched IDs
Mismatch = datacompy.Compare(df1, df2, join_columns='EMPLOYEE_ID')
# Appended both DF rows and Remove duplicates so Unmatched records will be return as Output
df3 = df1.append(df2)
Non_Matched_rows = df3.drop_duplicates(keep=False)
print(Non_Matched_rows.to_string())
Mismatch_1 = Mismatch.all_mismatch()  # Mismatched records
df4 = list(Mismatch_1)
col=0
for col in len(df4.columns):
    if df4[col + 1] != df4[col + 2]:
        print(df4[col + 1], df4[col + 2])
with pd.ExcelWriter("results3.xlsx") as writer:
    notInA.to_excel(writer, sheet_name="NotinDF2", index=False)
    notInB.to_excel(writer, sheet_name="NotinDF1", index=False)
    Mismatch_1.to_excel(writer, sheet_name="Mismatch Recs", index=False)
