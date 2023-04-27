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
r = red.read_yml
path=r"C:\Users\uma.adari\PycharmProjects\pythonProject4"

@When("read DB yaml info yaml files from {DB_Yaml} and {pathFolder}")
def step_readyaml(self, DB_Yaml,pathFolder):
    self.pathFolder=pathFolder
    self.db_data = r.read_file(path+"\\"+pathFolder+"\\"+ DB_Yaml)

@When("read {Query_yaml} file")
def step_readyaml(self,Query_yaml):
    self.db_qry = r.read_file(path+"\\"+self.pathFolder+"\\"+ Query_yaml)
    print(self.db_qry['Column_mapping']['EMPLOYEE_ID'])

# print(db_data['Db_conn']['Username']) # read username key value
@then("get Record count{DB}")
def step_connect(self, DB):
    self.a = self
    self.DB=DB
    os.environ['PATH'] = "C:\\oraclexe\\app\oracle\\instantclient_21_9"
    self.db_conn = cx_Oracle.connect(self.db_data[self.DB]['Username'], self.db_data[self.DB]['Password'],
                                     self.db_data[self.DB]['localHost'], cx_Oracle.SYSDBA)
    # db_conn=self.db_conn
    df_scount = pd.read_sql(self.db_qry['Query']['S_count'], self.db_conn)
    df_Tcount = pd.read_sql(self.db_qry['Query']['T_count'], self.db_conn)
    with pd.ExcelWriter(today_dt + "_countofrec.xlsx", mode="w") as writer:
        df_scount.to_excel(writer, sheet_name="SCountOf Recs", index=True)
        df_Tcount.to_excel(writer, sheet_name="TCountOf Recs", index=True)
@When("get Primary column Nulls")
def step_pkcheck(self):
    df_pk = pd.read_sql(self.db_qry['Query']['TGT_pk'], self.db_conn)
    print(df_pk)
@then("get Mismatched records")
def step_mismatch(self):
    df_src = pd.read_sql(self.db_qry['Query']['src_qry'],self.db_conn)
    df_tgt = pd.read_sql(self.db_qry['Query']['tgt_qry'],self.db_conn)

    mismatch = datacompy.Compare(df_src, df_tgt, join_columns='EMPLOYEE_ID')
    mismatch.matches(ignore_extra_columns=False)
    MisMatched_Rows = mismatch.all_mismatch()
    with pd.ExcelWriter(today_dt + "_MisMatch.xlsx", mode="w") as writer:
        MisMatched_Rows.to_excel(writer, sheet_name="Mismatch Recs", index=False)
        writer.save()
