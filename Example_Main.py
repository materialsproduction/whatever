'''
Created By Cameron Cunningham
for use during the HCC Git Demo
'''
def getInput():
    nums=[0]*2

    for i in range(0,2):
       nums[i] = input("Please enter a number:")
    return nums

def main():
    nums = getInput()
main()
