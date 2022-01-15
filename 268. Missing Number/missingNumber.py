class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Make a counter, this speeds everything up
        c = Counter(nums)
        #Check if num is in range len nums+1, if not, return it
        for num in range(len(nums)+1):
            if num not in c:
                return num 
        
        