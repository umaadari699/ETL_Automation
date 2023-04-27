import os

import cx_Oracle
import pandas as pd
import yaml
from yaml import SafeLoader
import re

class config:

    Spath = pd.read_csv(r'C:\Users\uma.adari\Downloads\Emp_Table.csv')
    Tpath = pd.read_csv(r'C:\Users\uma.adari\Downloads\Results.csv')
    Primary_Key = 'EMPLOYEE_ID'
    Drive_path = r'C:\Users\uma.adari\Downloads\\'
    srcfiles = ['sheet1_2023-02-19_132.csv','sheet2_2023-02-19.csv','Results.csv']
    TARGET = 'Emp_Table.csv'
    os.environ['PATH'] = "C:\\oraclexe\\app\oracle\\instantclient_21_9"
    con = cx_Oracle.connect("SYS", "Admin", "localhost/xe", cx_Oracle.SYSDBA)
    Getrecords_qry = "Select count(*) from HR.EMPLOYEES"

def write_data_w(data,sheet_name):
    name = str(sheet_name)
    with pd.ExcelWriter("Output.xlsx",mode="w") as writer:
      data.to_excel(writer, sheet_name=re.sub('[^a-zA-Z0-9]','',name), index=False)
      writer.save()

def testcase(sql):
    if(sql.equals=='Count'):
        query= 'Select count(*) from HR.employees'
        DBtarget = pd.read_sql(query)
    if(sql.equals=='Duplicate'):
        query='''select EMPLOYEE_ID,FIRST_NAME from HR.employees
              group by EMPLOYEE_ID,FIRST_NAME having count(*)>1'''
        DBtarget = pd.read_sql(query)









