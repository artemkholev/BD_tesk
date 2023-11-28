import psycopg2
from psycopg2 import Error

def psycopg2Actions(query):
  try:
    connection = psycopg2.connect(user="artem",
                                  password="TV",
                                  host="localhost",
                                  port="5432",
                                  database="demo")
    cursor = connection.cursor()
    if (query == 1):
      cursor.execute('SELECT vendorid, count(*) FROM taxi_yellow GROUP BY 1;')
      result = cursor.fetchall()
      print (result)
    elif (query == 2):
      cursor.execute('SELECT passenger_count, avg(total_amount) FROM taxi_yellow GROUP BY 1;')
      result = cursor.fetchall()
      print (result)
    elif (query == 3):
      cursor.execute('SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM taxi_yellow GROUP BY 1, 2;')
      result = cursor.fetchall()
      print (result)
    elif (query == 4):
      cursor.execute('SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance), count(*) FROM taxi_yellow GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;')
      result = cursor.fetchall()
      print (result)

  except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
  finally:
    if connection:
        cursor.close()
        connection.close()
        # print("Соединение с PostgreSQL закрыто")