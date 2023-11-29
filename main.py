from timeFunction import getTime 
from psycopg2_test import psycopg2Actions
from SQLite_test.SQLite_test import SQLiteActions
from DuckDB_test.DuckDB_test import DuckDBActions

numberIterations = 20
result1 = []
result2 = []
result3 = []
result4 = []

for i in range(0, numberIterations):
  # result1.append(getTime(psycopg2Actions, 1))
  # result2.append(getTime(psycopg2Actions, 2))
  # result3.append(getTime(psycopg2Actions, 3))
  # result4.append(getTime(psycopg2Actions, 4))
  
  # result1.append(getTime(SQLiteActions, 1))
  # result2.append(getTime(SQLiteActions, 2))
  # result3.append(getTime(SQLiteActions, 3))
  # result4.append(getTime(SQLiteActions, 4))

  result1.append(getTime(DuckDBActions, 1))
  result2.append(getTime(DuckDBActions, 2))
  result3.append(getTime(DuckDBActions, 3))
  result4.append(getTime(DuckDBActions, 4))

print('1 = ', result1, '\n')
print('2 = ', result2, '\n')
print('3 = ', result3, '\n')
print('4 = ', result4, '\n')