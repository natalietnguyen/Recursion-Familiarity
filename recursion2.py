#  File: recursion2.py 

#  Description: To define various recursive functions

#  Student Name: Natalie Nguyen

#  Student UT EID: ntn687

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 20 February, 2023

#  Date Last Modified: 22 February, 2023



# Given an array of ints, is it possible to choose a group of some 
# of the ints, such that the group sums to the given target? 
# This is a classic backtracking recursion problem. Once you 
# understand the recursive backtracking strategy in this problem, 
# you can use the same pattern for many problems to search a space 
# of choices. Rather than looking at the whole array, our convention 
# is to consider the part of the array starting at index start and 
# continuing to the end of the array. The caller can specify the 
# whole array simply by passing start as 0. No loops are needed -- 
# the recursive calls progress down the array. 
def groupSum(start, nums, target):
  # tests if function is at the end index
  if (start >= len(nums)):
    # returns boolean
    return (target == 0)
  else:
    # function calls itself; increases index and either subtracts or does not subtract the current number from target
    return (groupSum(start + 1, nums, target - nums[start])) or (groupSum(start + 1, nums, target))


  
# Given an array of ints, is it possible to choose a group of some 
# of the ints, beginning at the start index, such that the group 
# sums to the given target? However, with the additional constraint 
# that all 6's must be chosen. (No loops needed.)
def groupSum6(start, nums, target):
  # tests if function is at the end index
  if (start >= len(nums)):
    # returns boolean
    return (target == 0)
  # tests if current index of nums is equal to 6
  elif (nums[start] == 6):
    # function calls itself; increases index and subtracts 6 from the target
    return groupSum6(start + 1, nums, target - 6)
  else:
    # function calls itself; increases index and either subtracts or does not subtract the current number from target
    return (groupSum6(start + 1, nums, target - nums[start])) or (groupSum6(start + 1, nums, target))


  
# Given an array of ints, is it possible to choose a group of some 
# of the ints, such that the group sums to the given target with this 
# additional constraint: If a value in the array is chosen to be in 
# the group, the value immediately following it in the array must 
# not be chosen. (No loops needed.) 
def groupNoAdj(start, nums, target):
  # tests if function is at the end index
  if (start >= len(nums)):
    # returns boolean
    return (target == 0)
  else:
    # function calls itself; increases index by 2 if number is subtracted from the target
    # or increases index by 1 if number is not subtracted from the target
    return (groupNoAdj(start + 2, nums, target - nums[start])) or (groupNoAdj(start + 1, nums, target))



# Given an array of ints, is it possible to choose a group 
# of some of the ints, such that the group sums to the given 
# target with these additional constraints: all multiples of 
# 5 in the array must be included in the group. If the value 
# immediately following a multiple of 5 is 1, it must not 
# be chosen. (No loops needed.)
def groupSum5(start, nums, target):
  # tests if function is at the end index
  if (start >= len(nums)):
    # returns boolean
    return (target == 0)
  # tests if number at current index is a multiple of 5
  elif ((nums[start] % 5) == 0):
    # tests if number is at the last index
    if (start == len(nums) - 1):
      # function calls itself: index increases and number is subtracted from target
      return (groupSum5(start + 1, nums, target - nums[start]))
    else:
      # tests if the number adjacent to the number at the current index is 1
      if (nums[start + 1] == 1):
        # function calls itself: index increases by 2 in order to not choose 1 and number is subtracted from target
        return (groupSum5(start + 2, nums, target - nums[start]))
      else:
        # function calls itself: index increases and number is subtracted from target
        return (groupSum5(start + 1, nums, target - nums[start]))
  # if number at current index is not a multiple of 5
  else:
    # function calls itself; increases index and either subtracts or does not subtract the current number from target
    return (groupSum5(start + 1, nums, target - nums[start])) or (groupSum5(start + 1, nums, target))
  
  
  
# Given an array of ints, is it possible to choose a 
# group of some of the ints, such that the group sums 
# to the given target, with this additional constraint: 
# if there are numbers in the array that are adjacent 
# and the identical value, they must either all be chosen, 
# or none of them chosen. For example, with the array 
# [1, 2, 2, 2, 5, 2], either all three 2's in the middle 
# must be chosen or not, all as a group. (one loop can 
# be used to find the extent of the identical values). 
def groupSumClump(start, nums, target):
  # tests if function is at the end index
  if (start >= len(nums)):
    # returns boolean
    return (target == 0)
  else:
    # creates variable indicating number of adjacent identical numbers
    identical_count = 0

    # iterates through the indexes
    for i in range(start, len(nums) - 1):
      # tests if two adjacent numbers are identical
      if nums[i] == nums[i + 1]:
        # increases count
        identical_count += 1
      else:
        # exits loop
        break

    # tests if there are any adjacent identical numbers
    if identical_count > 0:
      # function calls itself: increases index by number of adjacent identical numbers and either subtracts or 
      # does not subtract all numbers from target
      return (groupSumClump(start + (identical_count + 1), nums, target - (nums[start] * (identical_count + 1)))) \
         or (groupSumClump(start + (identical_count + 1), nums, target))
    else:
      # function calls itself; increases index and either subtracts or does not subtract the current number from target
      return (groupSumClump(start + 1, nums, target - nums[start])) or (groupSumClump(start + 1, nums, target))
  
  

# Given an array of ints, is it possible to divide the 
# ints into two groups, so that the sums of the two 
# groups are the same. Every int must be in one group 
# or the other. Write a recursive helper method that 
# takes whatever arguments you like, and make the 
# initial call to your recursive helper from splitArray(). 
# (No loops needed.)
def splitArray(nums):
  # calls helper function
  return splitArrayHelper(nums, [], [], 0)

# Input: nums is an array of ints, b is a list, c is a list, idx is an 
#        int indicating the index in the nums list
# Output: a boolean indicating if it is possible to divide the 
#         ints into two groups, so that the sums of the two 
#         groups are the same
def splitArrayHelper(nums, b, c, idx):
  # tests if function is at the end index
  if (idx == len(nums)):
    # returns boolean
    return (sum(b) == sum(c))
  else:
    # creates a copy of lists b and c
    d = b[:]
    e = c[:]

    # adds number at current index to each list
    d.append(nums[idx])
    e.append(nums[idx])

    # function calls itself: index is increased and number at current index is added to list d or list e
    return (splitArrayHelper(nums, d, c, idx + 1)) or (splitArrayHelper(nums, b, e, idx + 1))

	
	
# Given an array of ints, is it possible to divide the 
# ints into two groups, so that the sum of one group
# is a multiple of 10, and the sum of the other group 
# is odd. Every int must be in one group or the other. 
# Write a recursive helper method that takes whatever 
# arguments you like, and make the initial call to your 
# recursive helper from splitOdd10(). (No loops needed.)
def splitOdd10(nums):
  # calls helper function
  return splitOdd10Helper(nums, [], [], 0)

# Input: nums is an array of ints, b is a list, c is a list, idx is an 
#        int indicating the index in the nums list
# Output: a boolean indicating if it is possible to divide the 
#         ints into two groups, so that the sum of one group
#         is a multiple of 10, and the sum of the other group 
#         is odd
def splitOdd10Helper(nums, b, c, idx):
  # tests if function is at the end index
  if (idx == len(nums)):
    # returns boolean
    return (((sum(b) % 10) == 0) and ((sum(c) % 2) == 1))
  else:
    # creates a copy of lists b and c
    d = b[:]
    e = c[:]

    # adds number at current index to each list
    d.append(nums[idx])
    e.append(nums[idx])

    # function calls itself: index is increased and number at current index is added to list d or list e
    return (splitOdd10Helper(nums, d, c, idx + 1)) or (splitOdd10Helper(nums, b, e, idx + 1))


  
# Given an array of ints, is it possible to divide the ints 
# into two groups, so that the sum of the two groups is the 
# same, with these constraints: all the values that are 
# multiple of 5 must be in one group, and all the values 
# that are a multiple of 3 (and not a multiple of 5) 
# must be in the other. (No loops needed.) 
def split53(nums):
  # calls helper function
  return split53Helper(nums, [], [], 0)

# Input: nums is an array of ints, b is a list, c is a list, idx is an 
#        int indicating the index in the nums list
# Output: a boolean indicating if it is possible to divide the 
#         ints into two groups, so that the sum of one group
#         is the same given constraints
def split53Helper(nums, b, c, idx):
  # tests if function is at the end index
  if (idx == len(nums)):
    # returns boolean
    return (sum(b) == sum(c))
  else:
    # creates a copy of lists b and c
    d = b[:]
    e = c[:]

    # tests if number at current index is a multiple of 5
    if ((nums[idx] % 5) == 0):
      # appends number to list d
      d.append(nums[idx])

      # function calls itself: index is increased and updated list is passed
      return split53Helper(nums, d, c, idx + 1)
    # tests if number at current index is a multiple of 3
    elif ((nums[idx] % 3) == 0):
      # appends number to list e
      e.append(nums[idx])

      # function calls itself: index is increased and updated list is passed
      return split53Helper(nums, b, e, idx + 1)
    # if number at current index is neither a multiple of 5 or 3
    else:
      # # adds number at current index to each list
      d.append(nums[idx])
      e.append(nums[idx])

      # function calls itself: index is increased and number at current index is added to list d or list e
      return (split53Helper(nums, d, c, idx + 1)) or (split53Helper(nums, b, e, idx + 1))



#######################################################################################################
#######################################################################################################
#                                                                                                     #
#                   DO NOT MODIFY ANYTHING BELOW THIS LINE !!                                         #
#                                                                                                     #
#######################################################################################################
#######################################################################################################
def main(argv):
    problems = ["groupSum", "groupSum6", "groupNoAdj", "groupSum5", "groupSumClump", "splitArray", "splitOdd10", "split53"]
    if len(argv) == 0:
        printHelp()
        exit(1)
    elif "all" in argv:
        argv = problems
    for problem in argv:
        if not problem in problems:
            printHelp()
            exit(1)
    
    groupSum_args = [(0, [2, 4, 8], 10), (0, [2, 4, 8], 14), (0, [2, 4, 8], 9), (0, [2, 4, 8], 8), (1, [2, 4, 8], 8), (1, [2, 4, 8], 2), (0, [1], 1), (0, [9], 1), (1, [9], 0), (0, [], 0), (0, [10, 2, 2, 5], 17), (0, [10, 2, 2, 5], 15), (0, [10, 2, 2, 5], 9)]
    groupSum6_args = [(0, [5, 6, 2], 8), (0, [5, 6, 2], 9), (0, [5, 6, 2], 7), (0, [1], 1), (0, [9], 1), (0, [], 0), (0, [3, 2, 4, 6], 8), (0, [6, 2, 4, 3], 8), (0, [5, 2, 4, 6], 9), (0, [6, 2, 4, 5], 9), (0, [3, 2, 4, 6], 3), (0, [1, 6, 2, 6, 4], 12), (0, [1, 6, 2, 6, 4], 13), (0, [1, 6, 2, 6, 4], 4), (0, [1, 6, 2, 6, 4], 9), (0, [1, 6, 2, 6, 5], 14), (0, [1, 6, 2, 6, 5], 15), (0, [1, 6, 2, 6, 5], 16)]
    groupNoAdj_args = [(0, [2, 5, 10, 4], 12), (0, [2, 5, 10, 4], 14), (0, [2, 5, 10, 4], 7), (0, [2, 5, 10, 4, 2], 7), (0, [2, 5, 10, 4], 9), (0, [10, 2, 2, 3, 3], 15), (0, [10, 2, 2, 3, 3], 7), (0, [], 0), (0, [1], 1), (0, [9], 1), (0, [9], 0), (0, [5, 10, 4, 1], 11)]
    groupSum5_args = [(0, [2, 5, 10, 4], 19), (0, [2, 5, 10, 4], 17), (0, [2, 5, 10, 4], 12), (0, [2, 5, 4, 10], 12), (0, [3, 5, 1], 4), (0, [3, 5, 1], 5), (0, [1, 3, 5], 5), (0, [3, 5, 1], 9), (0, [2, 5, 10, 4], 7), (0, [2, 5, 10, 4], 15), (0, [2, 5, 10, 4], 11), (0, [1], 1), (0, [9], 1), (0, [9], 0), (0, [], 0)]
    groupSumClump_args = [(0, [2, 4, 8], 10), (0, [1, 2, 4, 8, 1], 14), (0, [2, 4, 4, 8], 14), (0, [8, 2, 2, 1], 9), (0, [8, 2, 2, 1], 11), (0, [1], 1), (0, [9], 1)]
    splitArray_args = [([2, 2]), ([2, 3]), ([5, 2, 3]), ([5, 2, 2]), ([1, 1, 1, 1, 1, 1]), ([1, 1, 1, 1, 1]), ([]), ([1]), ([3, 5]), ([5, 3, 2]), ([2,2,10,10,1,1]), ([1,2,2,10,10,1,1]), ([1,2,3,10,10,1,1])]
    splitOdd10_args = [[5, 5, 5], [5, 5, 6], [5, 5, 6, 1], [6, 5, 5, 1], [6, 5, 5, 1, 10], [6, 5, 5, 5, 1], [1], [], [10, 7, 5, 5], [10, 0, 5, 5], [10, 7, 5, 5, 2], [10, 7, 5, 5, 1]]
    split53_args = [[1,1], [1, 1, 1], [2, 4, 2], [2, 2, 2, 1], [3, 3, 5, 1], [3, 5, 8], [2, 4, 6], [3, 5, 6, 10, 3, 3]]
	
	
    groupSum_ans = [True, True, False, True, True, False, True, False, True, True, True, True, True]
    groupSum6_ans = [True, False, False, True, False, True, True, True, False, False, False, True, True, False, False, True, True, False]
    groupNoAdj_ans = [True, False, False, True, True, True, False, True, True, False, True, True]
    groupSum5_ans = [True, True, False, False, False, True, True, False, False, True, False, True, False, True, True]
    groupSumClump_ans = [True, True, False, True, False, True, False]
    splitArray_ans = [True, False, True, False, True, False, True, False, False, True, True, False, True]
    splitOdd10_ans = [True, False, True, True, True, False, True, False, True, False, True, False]
    split53_ans = [True, False, True, False, True, False, True, True]

    for prob in argv:
      correct = 0  # counts number of test cases passed
      leftParen = "("
      rightParen = ")"
      # loop over test cases
      for i in range(len(locals()[prob+"_args"])):
        if type(locals()[prob+"_args"][i]) is tuple:
          leftParen = rightParen = ""
        if (type(locals()[prob+"_args"][i]) is str) or (type(locals()[prob+"_args"][i]) is int) or (type(locals()[prob+"_args"][i]) is list) or (len(locals()[prob+"_args"][i]) == 1): # function takes one argument
          if globals()[prob](locals()[prob+"_args"][i]) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](locals()[prob+"_args"][i])), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWrong!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](locals()[prob+"_args"][i])), " expected:", str(locals()[prob+"_ans"][i]))
        elif len(locals()[prob+"_args"][i]) == 2: # there are two arguments to function
          first, second = locals()[prob+"_args"][i]
          if globals()[prob](first, second) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second)), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWorng!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second)), " expected:", str(locals()[prob+"_ans"][i]))
        else:    
          first, second, third = locals()[prob+"_args"][i]
          if globals()[prob](first, second, third) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second, third)), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWrong!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second, third)), " expected:", str(locals()[prob+"_ans"][i]))
      print ("\n" + prob + ": passed", correct, "out of", len(locals()[prob+"_ans"]), "\n")

def printHelp():
    print ("\nInvoke this script with the name of the function you wish to test.")
    print ("e.g. python recursion1.py factorial")
    print ("Invoke with \"python recursion1.py all\" to run all of the function tests\n")
      
import sys
main(sys.argv[1:])
