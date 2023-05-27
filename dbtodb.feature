Feature: Verify Records in DB to DB

Scenario Outline: Verify Records in DB
  When read DB yaml info yaml files from <DB_Yaml> and <pathFolder>
  When read <Query_yaml> file
  Then get Record count<DB> from <src> and <tgt>
  When get Primary column Nulls
  Then get Mismatched records

   Examples:
     | src       | tgt       | DB_Yaml         | Query_yaml | pathFolder   | Date      | DB        |
     | employees | employees | DB_details.yaml | Data.yaml  | DbAutomation | 4-27-2023 | QA_DBconn |
