# from DbAutomation.steps import Config as co
# import pandas as pd
#
# # Here, Declaring Static things in Config Class and Inheriting them in This Queryexecute class
# connection = co.dbconnection
# def count_test():
#     df = pd.read_sql(connection.count, connection.con)
#     print("Query Ran Successfully")
#     print("Records Count", df.to_string(index=False))
#
# def Duplicate_test():
#     df_dup = pd.read_sql(connection.duplicate, connection.con)
#     if len(df_dup) > 0:
#         print('Yes It has Duplicate Records', len(df_dup))
#     else:
#         print('No Duplicate Records found', len(df_dup))
#
# def dataType_test():
#     df_dp = pd.read_sql(connection.Query,connection.con)
#     print(df_dp.info())
#
# def Null_check():
#     df_nlchk=pd.read_sql(connection.NullCheck,connection.con)
#     if len(df_nlchk) > 0:
#         print("Nulls present in PK column", df_nlchk)
#     else:
#         print("NO Nulls Identified in PK column", len(df_nlchk))
#
# #Reading Queries from EXCEL/CSV sheets
#
# def read_data_count():
#     print(connection.data.iloc[0,0])
#     df_rd=pd.read_sql(connection.data.iloc[0,0],connection.con)
#     print(df_rd.to_string(index=False))
#
#
# class execute:
#     dataType_test()
#     count_test()
#     Duplicate_test()
#     Null_check()
#     read_data_count()
