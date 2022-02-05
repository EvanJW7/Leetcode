class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Take care of a couple edge cases to speed up run time 
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        #Make an empty prefix to add to later
        prefix = ""
        first_word = strs[0]
        
        for i in range(len(first_word)):
            for word in strs:
                #If it is out of bounds or not equal to the same letter, return what prefix we have
                if i == len(word) or word[i] != first_word[i]:
                    return prefix
            #If that is not the case, continue to build the prefix 
            prefix += word[i]
        
        return prefix 
    
    
