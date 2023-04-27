import pandas as pd
from behave import *
import configuration_setUp as config

con = config.config


@given('Verify Primary key has Null values in table')
def PK_nullcheck(self):
    #  Null values check for PK
    self.pknull = con.Spath.loc[con.Spath[con.Primary_Key].isnull()]
    self.sum = self.pknull.shape[0]
    print(self.sum)


@then('then Print all null records in Excel sheet')
def Print_pknulls(self):
    if self.sum > 0:
        with pd.ExcelWriter("Duplicate.xlsx") as writer:
            self.pknull.to_excel(writer, sheet_name='Pk', index=False)
    else:
        print('Zero Nulls')


@when('Any column has Null values')
def Nulls_inAllcolumns(self):
    self.nullc = con.Spath[con.Spath.isnull().any(axis=1)]
    with pd.ExcelWriter("Duplicate.xlsx") as writer:
        self.nullc.to_excel(writer, sheet_name='NullsInAllCol', index=False)


@then('print all Null values count')
def print_Nullcount(self):
    print(con.Spath.isnull().sum())


@then('print all Non-Null counts wrt column')
def print_nonNull(self):
    self.srcnn = con.Spath.info()
    self.tgtnn = con.Tpath.info()
    with pd.ExcelWriter("Duplicate.xlsx") as writer:
        self.srcnn.to_excel(writer, sheet_name='SInfo', index=False)
        self.tgtnn.to_excel(writer, sheet_name='TInfo', index=False)
