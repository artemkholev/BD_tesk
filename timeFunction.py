import time

def getTime(psycopg2Actions, query): 
  start = time.time()
  psycopg2Actions(query)
  end = time.time()
  return ((end-start) * 10**3)