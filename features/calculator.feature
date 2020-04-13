Feature: The sum calculator

Scenario Outline: Get sum total
  Given a <values>
  When the calculator sums the values
  Then the <total> is correct

  Examples: values
  | values          | total |
  | 5,7             | 12    |
  | 5,3             | 8    |
