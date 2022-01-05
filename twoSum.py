class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Make an empty dictionary
        seen = {}
        
        #Iterate through the list of nums
        for i, num in enumerate(nums):
            #If the target-num in seen, return the index of target-num and the index of the number you are on
            if target-num in seen:
                return [seen[target-num], i]
            #If num from the numlist is not in seen, update the dictionary with the num and its index
            elif num not in seen:
                seen[num] = i
                