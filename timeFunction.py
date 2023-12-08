import time

def getTime(actions, query): 
  start = time.time()
  actions(query)
  end = time.time()
  return ((end-start) * 10**3)