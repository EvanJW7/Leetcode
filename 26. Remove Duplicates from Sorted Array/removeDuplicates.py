class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Initialize left pointer to 0
        lp = 0
        #Make a seen dictionary so we can account for the numbers we have already checked
        seen = {}
        #Initialize uniques to 0
        uniques = 0
        
        #Iterate through nums, if the num is not in seen, add it and increment lp and uniques.
        #Make sure to also specify what num goes in the index of lp
        for i, num in enumerate(nums):
            if num not in seen:
                seen[num] = i
                nums[lp] = num
                lp += 1
                uniques += 1
        #Return number of unique elements 
        return uniques