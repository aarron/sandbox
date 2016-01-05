# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.

def most_classes(teachers):
  topteacher = ""
  maxcount = 0
  currentcount = 0
  
  for key in teachers:
    currentcount = len(teachers[key])
    
    if currentcount > maxcount:
      maxcount = currentcount
      topteacher = key
  
  return topteacher


def num_teachers(teachers):
  totalteachers = len(teachers)
  
  return totalteachers


def stats(teachers):
  thelist = []
  
  for key in teachers:
    thelist.append([key, len(teachers[key])])
    
  return thelist