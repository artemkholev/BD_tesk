import duckdb

def DuckDBActions(query):
  try:
    conn = duckdb.connect('DuckDB_test/DuckDB.duckdb')
    cursor = conn.cursor()

    if (query == 1):
        cursor.sql('SELECT vendorid, count(*) FROM taxi GROUP BY 1;').show()
    elif (query == 2):
        cursor.sql('SELECT passenger_count, avg(total_amount) FROM taxi GROUP BY 1;').show()
    elif (query == 3):
        cursor.sql("SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM taxi GROUP BY 1, 2;").show()
    elif (query == 4):
        cursor.sql("SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM taxi GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;").show()
    cursor.close()
    conn.close()
  except duckdb.InvalidInputException as e:
    print(e)