'''Return the number of times that the string "hi" appears anywhere in the given string.'''

def count_hi(str):
  total=0
  for i in range(len(str)-1):
    if str[i:i+2]=='hi':
      total+=1
  return total