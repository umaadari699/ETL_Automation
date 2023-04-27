import logging

import configuration_setUp as configfile
from behave import *
import pandas as pd
import datacompy

dv = configfile.config()


@given(u'Get Source count')
def Src_count(self):
    self.scount = len(dv.Spath)
    print("The Source Records Count is", self.scount)


@when('get Target sheet Count')
def Tgt_count(self):
    self.tcount = len(dv.Tpath)
    print("The target Records Count is", self.tcount)


@then('Both Source and target should match')
def Records_count_Match(self):
    if self.scount == self.tcount:
        print("Source and targets records Matched")
    else:
        print("Records not Matched", self.scount,self.tcount)
        logging.info("Not Matched")
