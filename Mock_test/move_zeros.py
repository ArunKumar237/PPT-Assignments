"""
Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1

"""
l = [0,1,0,3,12]
def move_zeros(arr):
    pointer1 = 0 
    pointer2 = 1
    while pointer2<len(arr):
        if arr[pointer1]==0 and arr[pointer2]==0:
            pointer2 += 1
        if arr[pointer1]==0 and arr[pointer2]!=0:
            arr[pointer1],arr[pointer2] = arr[pointer2],arr[pointer1]
            pointer1 += 1
            pointer2 += 1 
    return(arr)

print(move_zeros(l))