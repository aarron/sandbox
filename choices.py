import random

def nchoices(l, n):
  l, n = list(l), int(n)
  
  for _ in range(n):
    thelist = list()
    thelist.append(random.choice(l))
    
  return thelist