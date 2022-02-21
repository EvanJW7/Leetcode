class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #Logic - we want to sort the list and make it a set to access the third to last index
        nums = sorted(set(nums))
        
        #If the sorted list has more than 3 or more elements, return thr third max
        if len(nums)>=3:
            return nums[-3]
        #Else, return the max
        else:
            return nums[-1]