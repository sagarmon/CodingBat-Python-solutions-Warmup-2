def last2(str):
  if len(str) < 2:
    return 0
  
  last2 = str[-2:]
  result = 0
  
  for i in range(len(str)-2):
    if last2 == str[i:i+2]:
      result += 1
  return result
