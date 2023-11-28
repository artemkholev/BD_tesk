import sqlite3
import csv

def SQLiteActions(query):
    try:
        connection = sqlite3.connect('SQLite_test/sqlite_python.db')
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
            cursor.execute("SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM taxi_yellow GROUP BY 1, 2;")
            result = cursor.fetchall()
            print (result)
        elif (query == 4):
            cursor.execute("SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM taxi_yellow GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;")
            result = cursor.fetchall()
            print (result)
        connection.close()
      
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (connection):
            connection.close()
            # print("Соединение с SQLite закрыто")