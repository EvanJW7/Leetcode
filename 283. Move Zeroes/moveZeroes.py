class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Make a j pointer
        j = 0
        #Enumerate the list of nums
        for i, num in enumerate(nums):
            #Match up the indexes you want
            if num != 0:
                nums[j] = nums[i]
                #If i is not the same a j, make it a 0, otherwise just keep going
                if i != j:
                    nums[i] = 0
                j += 1
        