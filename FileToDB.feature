Feature: Verify Records in File to DB

Scenario Outline: Verify Records in file and DB
  When Get DB yaml info yaml files from the <DB_Yaml> and <pathFolder>
  Then read <Query_yaml> file
  When get Latest <SRC> files from the folder <Date> and <DB> get Mismatched records


   Examples:
     | SRC                        | DB_Yaml         | Query_yaml | pathFolder   | Date      | DB      |
     | 2023-04-27_countofrec.xlsx | DB_details.yaml | Data.yaml  | DbAutomation | 4-27-2023 | Db_conn |
     | 2023-04-27_MisMatch.xlsx   | DB_details.yaml | Data.yaml  | DbAutomation | 4-27-2023 | Db_conn |
