'''Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as another of the values, it does not count towards the sum.'''

def lone_sum(a, b, c):
  if a==b and b==c:
    return 0
  if a==c:
    return b
  if a==b:
    return c
  if b==c:
    return a
  else:
    return a+b+c