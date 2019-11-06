'''
Created by Cameron Cunningham
for use during the HCC Git Demo
'''
def add(nums):
    return nums[0] + nums[1]
def subtract(nums):
    if nums[0] > nums[1]:
        return nums[0] - nums[1]
    else:
        return nums[1]-nums[0]
def multiply(nums):
    return nums[0] * nums[1]
def divide(nums):
    return nums[0] / nums[1]
