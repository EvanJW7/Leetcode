class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #Make an empty dictionary 
        storage = {}
        
        #Iterate through list of nums and add to the empty dictionary 
        for num in nums:
            #If the num is not in the dictionary, add it with a count of one
            if num not in storage:
                storage[num] = 1
            #If the num is already in the dictionary, delete it becuase it is not our answer 
            else:
                del storage[num]
                
        #Now we have a dictionary with one key:value pair and we want to return the key 
        return list(storage.keys())[0]