class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #All we need to do here is return the middle element in the sorted nums list as it will be the majority element 
        return sorted(nums)[len(nums)//2]
                