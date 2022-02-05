class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Take care of edge cases to speed up run time
        if len(nums) <= 1:
            return nums[0]
        
        #Make a variable called max_sum and make it equal to the first num in nums
        max_sum = nums[0]
        #Create a vriable called current_sum set to 0
        current_sum = 0
        
        #Iterate through the nums, use Kadane's algorithm to find the max sum 
        for num in nums:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
        