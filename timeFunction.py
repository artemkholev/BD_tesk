import time

def getTime(createPsycopg2): 
  start = time.time()
  createPsycopg2()
  

  end = time.time()
  print("The time of execution of above program is :", (end-start) * 10**3, "ms")