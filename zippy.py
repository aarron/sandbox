# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
# If you use .append(), you'll want to pass it a tuple of new values.

def combo(it1, it2):
  l1, l2 = list(it1), list(it2)
  mytups = ()
  
  for index, item in enumerate(l1):
    thetup = (l1[index], l2[index])
    mytups.append(thetup)
  
  return mytups