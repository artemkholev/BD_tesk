import psycopg2
import time

def createPsycopg2():
  a = 0
  for i in range(1000):
      a += (i**100)
 
def getTime(createPsycopg2): 
  start = time.time()
 
  createPsycopg2()
  

  end = time.time()
  print("The time of execution of above program is :", (end-start) * 10**3, "ms")

getTime(createPsycopg2)