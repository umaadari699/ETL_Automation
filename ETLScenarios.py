from datetime import datetime
import pandas as pd
import configuration_setUp as configfile
from behave import *
to_day = datetime.now()
today_dt = to_day.strftime('%Y-%m-%d')
print(today_dt)
Di = {}
a = configfile.config
print(len(a.srcfiles))


@When("Print Record count in {SRC} and {TGT} file or table")
def SRC_Count(self, SRC, TGT):
    self.S = pd.read_csv(a.Drive_path + SRC)
    self.T = pd.read_csv(a.Drive_path + TGT)
    self.s_count = self.S.count()
    self.t_count = len(self.T)
    print('Source Count is ', self.s_count, 'Target Count is ', self.t_count)
    fl = SRC.split(".")
    with pd.ExcelWriter(fl[0] + today_dt + "_file.xlsx", mode="w") as writer:
        self.s_count.to_excel(writer, sheet_name=SRC, index=True)
        writer.save()


@when('print duplicate records in {SRC} and {TGT} file or table')
def Duplicate_check(self, SRC, TGT):
    self.S = pd.read_csv(a.Drive_path + SRC)
    self.T = pd.read_csv(a.Drive_path + TGT)
    self.s_dups = self.S[self.S.duplicated()]
    self.T_dups = self.T[self.T.duplicated()]
    fn = SRC.split(".")
    with pd.ExcelWriter(fn[0] + today_dt + "dup_file.xlsx", mode="w") as writer:
        self.s_dups.to_excel(writer, sheet_name=SRC, index=False)
        self.T_dups.to_excel(writer, sheet_name=TGT, index=False)
        writer.save()


@when('Print Primary column Nulls in {SRC} and {TGT} file or table')
def Primary_nullcheck(self, SRC, TGT):
    self.src = SRC
    print(self.src)


@when('Print Mismatched records between {SRC} and {TGT} file or table')
def Mismatch_rec(self, SRC, TGT):
    print('c')


@then('Compare Metadata {SRC} and {TGT} file or table')
def Metadata_comp(self, SRC, TGT):
    print('d')
