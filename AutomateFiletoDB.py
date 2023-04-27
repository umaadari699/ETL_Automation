import glob
import os
import cx_Oracle
import datacompy
from datetime import datetime

today = datetime.today()
today_dt = today.strftime('%Y-%m-%d')
import pandas as pd
import yaml
from behave import *
import readyaml as red
global path
r = red.read_yml
path = r"C:\Users\uma.adari\PycharmProjects\pythonProject4"

@when("Get DB yaml info yaml files from the {DB_Yaml} and {pathFolder}")
def yamlfiles(self, pathFolder, DB_Yaml):
    self.pathFolder = pathFolder
    self.db_data = r.read_file(path + "\\" + pathFolder + "\\" + DB_Yaml)


@then("read {Query_yaml} file")
def read_ymlfile(self, Query_yaml):
    self.db_qry = r.read_file(path + "\\" + self.pathFolder + "\\" + Query_yaml)

@when("get Latest {SRC} files from the folder {Date} and {DB} get Mismatched records")
def getdata(self, SRC, Date, DB):
    self.Date=Date
    self.SRC=SRC
    self.DB=DB
    df_src = pd.read_excel(path + '\\' + self.Date + '\\' + self.SRC)
    os.environ['PATH'] = "C:\\oraclexe\\app\oracle\\instantclient_21_9"
    self.db_conn = cx_Oracle.connect(self.db_data[self.DB]['Username'], self.db_data[self.DB]['Password'],
                                     self.db_data[self.DB]['localHost'], cx_Oracle.SYSDBA)
    df_Tgt = pd.read_sql(self.db_qry['Query']['src_qry'], self.db_conn)
    mismatch_src = datacompy.Compare(df_src, df_Tgt, join_columns='EMPLOYEE_ID')
    mismatch_src.matches(ignore_extra_columns=False)
    df1_unq = mismatch_src.df1_unq_rows
    df2_unq = mismatch_src.df2_unq_rows
    MisMatched_S = mismatch_src.all_mismatch() # Gives Mismatched data for Matched columns on Employee_ID
    concat_res=pd.concat([df_src,df_Tgt]).drop_duplicates(keep=False)
    fl = SRC.split(".")
    pathforReport=r"C:\Users\uma.adari\PycharmProjects\pythonProject4\Results"
    with pd.ExcelWriter(pathforReport +'\\'+fl[0] + today_dt + "_MisMfilevsDb1.xlsx", mode="w") as writer:
        MisMatched_S.to_excel(writer, sheet_name="Mismatched_data", index=False)
        df1_unq.to_excel(writer, sheet_name="Extra in DF1", index=False)
        concat_res.to_excel(writer, sheet_name="concat", index=False)
        df2_unq.to_excel(writer, sheet_name="Extra in DF2", index=False)
        writer.save()
