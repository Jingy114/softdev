def string_times(str, n):
  return n * str

def front_times(str, n):
  if len(str) > 2:
    return n * str[0:3]
  else:
    return n * str

def string_bits(str):
  final = ""
  increment = 0
  while increment < len(str): 
    final += str[increment] 
    increment += 2
  return final
    
def string_splosion(str):
  result = "" 
  counter = 1
  while counter <= len(str): 
    result += str[0:counter] 
    counter += 1
  return result 

def last2(str):
  last2 = str[-2:] 
  counter = 0
  result = 0 
  while counter < len(str)-2: 
    if str[counter: counter + 2] == last2: 
      result += 1
    counter += 1
  return result

def array_count9(nums):
  counter = 0
  for x in nums: 
    if x == 9: 
      counter += 1
  return counter

def array_front9(nums):
  index = 0
  counter = 0
  if len(nums) >= 4: 
    while index <= 3: 
      if nums[index] == 9:
        counter += 1
        index += 1
      else: 
        index += 1
  else: 
    while index <= len(nums)-1: 
      if nums[index] == 9:
        counter += 1
        index += 1
      else: 
        index += 1
  # after both cases run 
  if counter != 0:
      return True
  else: 
      return False

def array123(nums):
  index = 0
  while index <= len(nums)-3: 
    if nums[index: index + 3] == [1,2,3]: 
      return True
    else: 
      index += 1
  return False

def string_match(a, b):
  index = 0
  counter = 0
  while index <= len(a)-2: 
    if a[index:index+2] == b[index:index+2]: 
      counter += 1
      index += 1
    else: 
      index += 1
  return counter
