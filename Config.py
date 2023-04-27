import os
import re
import cx_Oracle
import pandas as pd
from reportlab.pdfgen import canvas

class dbconnection:
    tabel_name="HR.EMPLOYEES"
    os.environ['PATH'] = "C:\\oraclexe\\app\oracle\\instantclient_21_9"
    con = cx_Oracle.connect("SYS", "Admin", "localhost/xe", cx_Oracle.SYSDBA)
    Query = "Select * from HR.EMPLOYEES"
    count = "Select count(*) from "+tabel_name
    duplicate = '''select EMPLOYEE_ID,FIRST_NAME from HR.EMPLOYEES 
    group by EMPLOYEE_ID,FIRST_NAME having count(*) >1'''
    NullCheck = "Select * from HR.EMPLOYEES where EMPLOYEE_ID is NULL"

    # Let me Try Above method in different Ways, Like Read data from Excel sheet
    data= pd.read_excel(r'C:\Users\uma.adari\Downloads\Events.xlsx',sheet_name="Q",index_col=0)

def write_data(data, sheet_name):
    name = str(sheet_name)
    with pd.ExcelWriter("Output.xlsx") as writer:
        data.to_excel(writer, sheet_name=re.sub('[^a-zA-Z0-9]', '', name), index=False)


