import cx_Oracle
import os
import pandas as pd
import configuration_setUp as config
from reportlab.pdfgen import canvas

from self import self
c = config.config.con
def Getallrecords_execute(con):
    sql = config.config.Getrecords_qry
    print(sql)
    df = pd.read_sql(sql,con)
    print(df)
    pdf = canvas.Canvas("report.pdf")
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 750, "Customer Report")
    pdf.setFont("Helvetica", 12)
    y = 700
    l= len(df)
    pdf.drawString(50,y - 60,"Records Count is" + str(l))
    pdf.drawString(50,y - 80,"Records Count is" + str(l))
    pdf.save()
class dbconnection:
    os.environ['PATH'] = "C:\\oraclexe\\app\oracle\\instantclient_21_9"
    con = cx_Oracle.connect("SYS", "Admin", "localhost/xe", cx_Oracle.SYSDBA)
    print("Connected VVV")
    Getallrecords_execute(con)



