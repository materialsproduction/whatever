'''
Created By Cameron Cunningham
for use during the HCC Git Demo
'''
def getInput():
    nums=[0]*2

    for i in range(0,2):
       nums[i] = input("Please enter a number:")
    return nums

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



def main():
    nums = getInput()
    print(add(nums))
    print(subtract(nums))
    print(multiply(nums))
    print(divide(nums))
    
main()
