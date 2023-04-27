Feature: Verify Records and All Other ETL scenarios b/w SRC and TGT

Scenario Outline: Count of Records in SRC & TGT
  When Print Record count in <SRC> and <TGT> file or table
  When print duplicate records in <SRC> and <TGT> file or table
  When Print Primary column Nulls in <SRC> and <TGT> file or table
  When Print Mismatched records between <SRC> and <TGT> file or table
  Then Compare Metadata <SRC> and <TGT> file or table

  Examples:
    | SRC         | TGT           |
    | sheet1.csv  | Emp_Table.csv |
    | sheet2.csv  | Emp_Table.csv |
    | Results.csv | Emp_Table.csv |







