import pandas as pd
import sqlalchemy
from behave import *
import cx_Oracle
import os

@given('User entered DB Username and password')
def step_impl(context):
    try:
        os.environ['PATH'] = "C:\\oraclexe\\app\oracle\\instantclient_21_9"
        db = cx_Oracle.connect("SYS", "Admin", "localhost/xe", cx_Oracle.SYSDBA)
        print("Connected XXX")
        cursor = db.cursor()
        sql = "select * from HR.EMPLOYEES"
        cursor.execute(sql)
        result = cursor.fetchall()
        df = pd.read_sql(sql, db)

    except Exception as er:
        print('Error:', er)

@when('User connected to database sucessfully')
def step_impl(context):
    print("connected to database sucessfully")


@then('Retrieve Some details from database')
def step_impl(context):
    try:
        print('DataFrame is written successfully to the Excel File.')

    except Exception as er:
        print('Error:', er)
