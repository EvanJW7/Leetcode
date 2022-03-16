class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        Logic - we want to make a seen dictionary and solve the problem by the time the seen dictionary is complete. We do not build a dictionary
        first and then loop through it, we can find a solution while in the process of building the dictionary. We want to loop through each num in 
        nums and check if the target-num is in our dictionary. If it is, we have a paring and we can return their indexes. If not, add it to the 
        dictionary.
        '''
        
        #Make an empty dictionary
        seen = {}
        
        #Iterate through the list of nums
        for i, num in enumerate(nums):
            #If the target-num in seen, return the index of target-num and the index of the number you are on
            if target-num in seen:
                return [seen[target-num], i]
            #If not, add to dictionary
            else:
                seen[num] = i
                
