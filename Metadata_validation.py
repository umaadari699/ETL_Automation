import pandas as pd
from behave import *
import configuration_setUp as config

con = config.config

@given('get meta data of Source')
def Src_metadata(self):
   self.src = con.Spath.info()

@When('get meta data of Target')
def Tgt_metadata(self):
   self.tgt = con.Tpath.info()

@then('Verify both are same or not')
def Match_metadata(self):
   if self.src == self.tgt:
      print('Both are Matched')
   else:
      print("Not Matched")
