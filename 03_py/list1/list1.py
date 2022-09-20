def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6

def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[len(nums)-1] 

def make_pi():
  pi = [3, 1, 4] 
  return pi 

def common_end(a, b):
  return a[0] == b[0] or a[len(a)-1] == b[len(b)-1] 

def sum3(nums):
  sum = 0
  for x in nums: 
    sum += x
  return sum 

def rotate_left3(nums):
  result = [ nums[1], nums[2], nums[0]]
  return result
  
def reverse3(nums):
  result = [ nums[2], nums[1], nums[0]]
  return result

def max_end3(nums):
  counter = 0
  largest = 0
  if nums[0] > nums[len(nums)-1]: 
    largest = nums[0]
  else: 
    largest = nums[len(nums)-1]
   # replace !
   return [largest,largest,largest] 
 
def sum2(nums):
  counter = 0
  sum = 0
  if len(nums) == 0:
    return 0
  else: 
    if len(nums) < 2: 
      for x in nums: 
        sum += x
    else: 
      sum = sum + nums[0] + nums[1] 
  return sum 
      
def middle_way(a, b):
  middle = [ a[1], b[1]]
  return middle

def make_ends(nums):
  ends = [nums[0], nums[len(nums)-1]] 
  return ends

def has23(nums):
  return (nums[0] == 2 or nums[0] == 3) or (nums[1] == 2 or nums[1] == 3)
