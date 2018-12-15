'''Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".'''

def first_half(str):
  total=len(str)
  return str[:total/2]