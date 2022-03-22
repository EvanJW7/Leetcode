class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #We want to first sort the list so we can traverse it more easily
        nums.sort()
        triplets = []
        
        #Take care of edge case
        if nums == []:
            return []
        #Loop through the nums and use a three pointer strategy with the left pointer
        #being one to the right of the num you are on.
        for i in range(len(nums)-2):
            lp = i+1
            rp = len(nums)-1
            while lp<rp:
                mySum = nums[i]+nums[lp]+nums[rp]
                if mySum >0:
                    rp -= 1
                elif mySum < 0:
                    lp += 1
                elif mySum == 0:
                    if [nums[i], nums[lp], nums[rp]] not in triplets:
                        triplets.append([nums[i], nums[lp], nums[rp]])
                    lp += 1
                    rp -= 1
                    
        return triplets 