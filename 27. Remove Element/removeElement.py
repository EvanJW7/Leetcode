class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Initialize a variable to 0
        j = 0
        #Enumerate the nums list
        #Logic: if the num is the val, don't do anything. i will increment by one and restart the loop.
        #If the num is not the val: make the num at the ith place equal to the num at jth place. Then increment j by one
        #This will fill the spots taken up by the val with a number not the val since i and j are different
        for i, num in enumerate(nums):
            if num != val:
                nums[j] = nums[i]
                j += 1
        #j also can serve as a count variable, as it will tell us how many variables were not the val
        #We can simply return j
        return j
        