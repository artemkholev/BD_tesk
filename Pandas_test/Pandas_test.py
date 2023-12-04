import pandas
import sqlite3 
import duckdb

def PandasActions(query):
  try:
    connection = sqlite3.connect('Pandas_test/pandas_python.db')

    if (query == 1):  
      data = pandas.read_sql_query('SELECT vendorid, count(*) FROM taxi_yellow GROUP BY 1;', connection) 
      print(data) 
    elif (query == 2):
      data = pandas.read_sql_query('SELECT passenger_count, avg(total_amount) FROM taxi_yellow GROUP BY 1;', connection) 
      print(data) 
    elif (query == 3):
      data = pandas.read_sql_query("SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM taxi_yellow GROUP BY 1, 2;", connection) 
      print(data) 
    elif (query == 4):
      data = pandas.read_sql_query("SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM taxi_yellow GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;", connection) 
      print(data) 

    connection.close()
    
  except sqlite3.Error as error:
      print("Ошибка при подключении к sqlite", error)
  finally:
      if (connection):
          connection.close()
          # print("Соединение с SQLite закрыто")


  # try:
  #   conn = duckdb.connect('/home/artem-kholev/Desktop/bd3/DuckDB_test/DuckDB.duckdb')

  #   if (query == 1):  
  #     data = pandas.read_sql_query('SELECT vendorid, count(*) FROM taxi GROUP BY 1;', conn) 
  #     print(data) 
  #   elif (query == 2):
  #     data = pandas.read_sql_query('SELECT passenger_count, avg(total_amount) FROM taxi GROUP BY 1;', conn) 
  #     print(data) 
  #   elif (query == 3):
  #     data = pandas.read_sql_query("SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM taxi GROUP BY 1, 2;", conn) 
  #     print(data) 
  #   elif (query == 4):
  #     data = pandas.read_sql_query("SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM taxi GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;", conn) 
  #     print(data) 

  #   conn.close()
  # except duckdb.InvalidInputException as e:
  #   print(e)