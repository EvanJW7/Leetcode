class Solution:
    def rob(self, nums: List[int]) -> int:
        #Take care of edge case
        if len(nums) == 1:
            return nums[0]
        #Make a new array of the same length as nums
        mynums = nums
        #We know the max of the first number is just the first number
        mynums[0] = nums[0]
        #The second index of the new array is the max of the first and second number of nums
        mynums[1] = max(nums[0], nums[1])
        
        #Now we loop through the rest of the numbers and update the maxes we have seen.
        #We can either take the current number plus the number at index-2 or the number at index-1
        for num in range(2, len(nums)):
            mynums[num] = max(mynums[num-1], mynums[num]+mynums[num-2])
            
        #Return the number at the last index(which will be the max)
        return mynums[-1]
            
        