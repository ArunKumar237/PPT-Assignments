#!/usr/bin/env python
# coding: utf-8

# **Question 1:**
# Given an integer array nums of length n and an integer target, find three integers
# in nums such that the sum is closest to the target.
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.
# 
# **Example 1:**
# ```
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# ```
# **Explanation:** The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# In[9]:


def threeSumClosest(nums, target):
        nums.sort()
        return KSumClosest(nums, 3, target)

def KSumClosest(nums, k, target):
    N = len(nums)
    if N == k:
        return sum(nums[:k])

    # target too small
    current = sum(nums[:k])
    if current >= target:
        return current
    
    # target too big
    current = sum(nums[-k:])
    if current <= target:
        return current

    if k == 1:
        return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]

    closest = sum(nums[:k])
    for i, x in enumerate(nums[:-k+1]):
        if i>0 and x == nums[i-1]:
            continue
        current = KSumClosest(nums[i+1:], k-1, target - x) + x
        if abs(target - current) < abs(target - closest):
            if current == target:
                return target
            else:
                closest = current

    return closest


# In[10]:


threeSumClosest([-1,2,1,-4],1)


# ---

# **Question 2:**
# Given an array nums of n integers, return an array of all the unique quadruplets
# [nums[a], nums[b], nums[c], nums[d]] such that:
# ```
#            ● 0 <= a, b, c, d < n
#            ● a, b, c, and d are distinct.
#            ● nums[a] + nums[b] + nums[c] + nums[d] == target
# ```
# You may return the answer in any order.
# 
# **Example 1:**
# ```
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# ```

# In[13]:


def fourSum(nums, target):
    nums.sort()
    results = []
    helper(nums, target, 4, [], results)
    return results

def helper(nums, target, N, res, results):

    if len(nums) < N or N < 2: #1
        return
    if N == 2: #2
        output_2sum = twoSum(nums, target)
        if output_2sum != []:
            for idx in output_2sum:
                results.append(res + idx)

    else: 
        for i in range(len(nums) -N +1): #3
            if nums[i]*N > target or nums[-1]*N < target: #4
                break
            if i == 0 or i > 0 and nums[i-1] != nums[i]: #5
                helper(nums[i+1:], target-nums[i], N-1, res + [nums[i]], results)


def twoSum(nums, target):
    res = []
    left = 0
    right = len(nums) - 1 
    while left < right: 
        temp_sum = nums[left] + nums[right] 

        if temp_sum == target:
            res.append([nums[left], nums[right]])
            right -= 1
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while right > left and nums[right] == nums[right + 1]:
                right -= 1

        elif temp_sum < target: 
            left +=1 
        else: 
            right -= 1

    return res


# In[14]:


fourSum([1,0,-1,0,-2,2],0)


# ---

# **Question 3:**
# A permutation of an array of integers is an arrangement of its members into a
# sequence or linear order.
# 
# For example, for arr = [1,2,3], the following are all the permutations of arr:
# [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# 
# The next permutation of an array of integers is the next lexicographically greater
# permutation of its integer. More formally, if all the permutations of the array are
# sorted in one container according to their lexicographical order, then the next
# permutation of that array is the permutation that follows it in the sorted container.
# 
# If such an arrangement is not possible, the array must be rearranged as the
# lowest possible order (i.e., sorted in ascending order).
# ```
# ● For example, the next permutation of arr = [1,2,3] is [1,3,2].
# ● Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# ● While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
# have a lexicographical larger rearrangement.
# ```
# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.
# 
# **Example 1:**
# ```
# Input: nums = [1,2,3]
# Output: [1,3,2]
# ```
# 

# In[43]:


def permute(nums):
    def backtrack(first=0):
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output

arr = [1, 2, 3]
permutations = permute(arr)
print(permutations[-1])


# ---

# **Question 4:**
# Given a sorted array of distinct integers and a target value, return the index if the
# target is found. If not, return the index where it would be if it were inserted in
# order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# **Example 1:**
# ```
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# ```

# In[44]:


def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


# In[46]:


arr = [1, 3, 5, 6]
target = 5
insert_index = searchInsert(arr, target)
print(insert_index)


# ---

# **Question 5**
# You are given a large integer represented as an integer array digits, where each
# digits[i] is the ith digit of the integer. The digits are ordered from most significant
# to least significant in left-to-right order. The large integer does not contain any
# leading 0's.
# 
# Increment the large integer by one and return the resulting array of digits.
# 
# **Example 1:**
# 
# ``
# Input: digits = [1,2,3]
# Output: [1,2,4]
# ``
# 
# **Explanation:** The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# In[47]:


def plusOne(digits):
    n = len(digits)
    
    for i in range(n-1, -1, -1):
        digits[i] += 1
        
        if digits[i] == 10:
            digits[i] = 0
        else:
            return digits
    
    digits.insert(0, 1)
    return digits


# In[49]:


arr = [1,2,3]
result = plusOne(arr)
print(result)


# ---

# **Question 6:**
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.
# 
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
# 
# **Example 1:**
# ```
# Input: nums = [2,2,1]
# Output: 1
# ```

# In[52]:


def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


# In[54]:


arr = [2, 2, 1]
single = singleNumber(arr)
print(single)


# ---

# **Question 7:**
# You are given an inclusive range [lower, upper] and a sorted unique integer array
# nums, where all elements are within the inclusive range.
# 
# A number x is considered missing if x is in the range [lower, upper] and x is not in
# nums.
# 
# Return the shortest sorted list of ranges that exactly covers all the missing
# numbers. That is, no element of nums is included in any of the ranges, and each
# missing number is covered by one of the ranges.
# 
# **Example 1:**
# ```
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: [[2,2],[4,49],[51,74],[76,99]]
# ```
# **Explanation:**
# ```
# The ranges are:
# [2,2]
# [4,49]
# [51,74]
# [76,99]
# ```

# In[59]:


def findMissingRanges(nums, lower, upper):
    def formatRange(start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + "," + str(end)
    
    ranges = []
    
    prev = lower - 1
    
    for num in nums:
        if num > prev + 1:
            ranges.append(formatRange(prev + 1, num - 1))
        prev = num
    
    if upper > prev:
        ranges.append(formatRange(prev + 1, upper))
    
    return ranges


# In[61]:


arr = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(arr, lower, upper)
print(result)


# ---

# **Question 8**
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.
# 
# **Example 1:**
# ```
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# ```

# In[62]:


def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals by start time
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    
    return True


# In[63]:


intervals = [[0, 30], [5, 10], [15, 20]]
result = canAttendMeetings(intervals)
print(result)


# In[ ]:




