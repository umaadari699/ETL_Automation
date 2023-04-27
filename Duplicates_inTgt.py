import configuration_setUp as configu
import pandas as pd
from behave import *
import datacompy
a = configu.config
@given('Get duplicate records from Source')
def Src_Duplicate_Check(self):
     self.Sdupcheck = a.Spath[a.Spath.duplicated()]

@when('Target table has Duplicate')
def Tgt_duplicate_Check(self):
   self.Tdupcheck = a.Tpath[a.Tpath.duplicated()]

@then('get records which Occurrence >1 in Source')
def Src_rec_occurrence(self):
    recoccS = a.Spath.groupby(['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL']).EMPLOYEE_ID.size()
    self.S = recoccS[recoccS > 1]

@then('get records which Occurrence >1 in Target')
def Tgt_rec_occurrence(self):
    recoccT = a.Tpath.groupby(['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL']).EMPLOYEE_ID.size()
    self.T = recoccT[recoccT > 1]
@then('Count of Duplicates in SRC')
def dup_count_src(self):
   self.S_count = a.Spath[['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL']].duplicated().sum()
   print(self.S_count)

@then('Count of Duplicates in TGT')
def dup_count_Tgt(self):
    T_count = a.Tpath[['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL']].duplicated().sum()
    print(T_count)

@then('Print all duplicated records in Excel')
def print_duplicates(self):
    with pd.ExcelWriter("Duplicate.xlsx") as writer:
        self.Sdupcheck.to_excel(writer,sheet_name='Sduplicates',index=False)
        self.Tdupcheck.to_excel(writer,sheet_name='Tduplicates',index=False)

