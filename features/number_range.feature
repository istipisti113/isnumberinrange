Feature: Szám tartomány ellenőrzése
  Mint felhasználó
  Szeretném ellenőrizni, hogy egy szám egy adott tartományban van-e
  Hogy validációt végezhessek

Scenario Outline: Is the number in range
  Given the number is "<number>"
  And the minimum is "<min>"
  And the maximum is "<max>"
  When I check if the number is in range
  Then the result shall be "<result>"

Examples:
| number | min | max | result |
| 5 | 0 | 10 | True |
| 0 | 5 | 10 | False |
| 15 | 0 | 10 | False |
| 0 | 5 | 5 | False |
| 5 | 5 | 5 | True |
|2.5|0|5|True|
|-5|-10|0|True|