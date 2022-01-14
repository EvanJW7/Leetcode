class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Return a boolean whether the length of the set of nums is less than length of nums
        #If this is true, that means there was a duplicate 
        return len(set(nums)) < len(nums)