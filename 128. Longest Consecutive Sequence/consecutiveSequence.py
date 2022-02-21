class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Logic - we want to return the most amount of consecutive integers from the nums list
        #Take care of edge cases
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        #Make nums into a set, make a maxCount variable set to 0
        nums = set(nums)
        maxCount = 0
        
        #Check every num in nums if it is the start of a sequence or not
        for n in nums:
            if n-1 not in nums:
                #If the num is the start of a sequence, keep adding one to it until it is no longer in nums
                #Start count at one since the number we are starting with counts
                count = 1
                while n+1 in nums:
                    n += 1
                    count += 1
                #Compute the max count you got from the sequence you just checked
                maxCount = max(count, maxCount)
                
        #Return the maxCount
        return maxCount
                    