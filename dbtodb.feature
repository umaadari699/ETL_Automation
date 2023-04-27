Feature: Verify Records in DB to DB

Scenario Outline: Verify Records in DB
  When read DB yaml info yaml files from <DB_Yaml> and <pathFolder>
  When read <Query_yaml> file
  Then get Record count<DB>
  When get Primary column Nulls
  Then get Mismatched records

   Examples:
     | DB_Yaml         | Query_yaml | pathFolder   | Date      | DB      |
     | DB_details.yaml | Data.yaml  | DbAutomation | 4-27-2023 | Db_conn |
