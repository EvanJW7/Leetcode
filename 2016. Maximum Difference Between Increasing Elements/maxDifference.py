class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        #Start off with the maxD being -1 since that is what we will return is no such maxD exists
        maxD = -1
        #Use a two pointer approach to compare the items in the nums list
        lp, rp = 0, 1
        #Look through the nums in the nums list, check their max difference. Make sure lp is less than rp
        while rp < len(nums):
            if nums[lp]<nums[rp]:
                maxD = max(maxD, nums[rp]-nums[lp])
            #If lp is greater than rp, we have found a new min. Make lp equal to rp and keep looping
            else:
                lp = rp
            #rp gets incremented no matter what   
            rp += 1
            
        return maxD