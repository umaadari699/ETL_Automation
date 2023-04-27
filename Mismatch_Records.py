from datetime import datetime

import configuration_setUp as configfile
from behave import *
import pandas as pd
import datacompy
Con = configfile.config
today = datetime.today()
today_dt = today.strftime('%Y-%m-%d')
#@Given('Get the Mismatched row values for matched IDS')

def missed_records():
    # Based on Emp id, Retrieving all mismatched row values of matched emp Ids
    mismatch = datacompy.Compare(Con.Spath, Con.Tpath, join_columns='EMPLOYEE_ID')
    mismatch.matches(ignore_extra_columns=False)
    MisMatched_Rows = mismatch.all_mismatch()
    with pd.ExcelWriter(today_dt+"_MisMatch.xlsx",mode="w") as writer:
        MisMatched_Rows.to_excel(writer, sheet_name="Mismatch Recs", index=False)
        writer.save()

def count_records():
    count = Con.Spath.count()
    print("SRC Count", count)
    with pd.ExcelWriter(today_dt+"_RecCount.xlsx",mode="w") as writer:
        count.to_excel(writer, sheet_name='SrcCount', index=True)
        writer.save()
#@then('Identify which records are not present in Source')
def Missed_inSource():
    # put all columns so that each and every column and Row values will verify
    Report = datacompy.Compare(Con.Spath, Con.Tpath,
                               join_columns=['EMPLOYEE_ID'] )#'first_name', 'last_name', 'email',
                               #               'phone_number', 'hire_date', 'job_id', 'salary',
                               #               'commission_pct', 'manager_id', 'department_id'])
    missedin_Src = Report.df2_unq_rows # only present in df2 means not in Source df1
    with pd.ExcelWriter(today_dt+"_MisInSRC.xlsx",mode="w") as writer:
        missedin_Src.to_excel(writer, sheet_name='NotInSource', index=False)
        writer.save()

    # Returns which are not present in Target
#@then('Identify Which records are not Present in target')
def Missed_inTarget(): # SRC - TGT
    Report = datacompy.Compare(Con.Spath, Con.Tpath,
                                join_columns=['EMPLOYEE_ID']) #, 'first_name', 'last_name', 'email',
                               #               'phone_number', 'hire_date', 'job_id', 'salary',
                               #               'commission_pct', 'manager_id', 'department_id'])
    missedin_Tgt = Report.df1_unq_rows # Means, return records Only present in df1 means not in df2
    with pd.ExcelWriter(today_dt+"_MisInTGT.xlsx", mode='w') as writer:
      missedin_Tgt.to_excel(writer, sheet_name='NotInTarget', index=False)

class mr:
    missed_records()
    Missed_inSource()
    Missed_inTarget()
    count_records()
