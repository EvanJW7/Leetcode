class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Take care of a couple edge cases to speed up run time 
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        #Logic: we are using the first word as the prefix and comparing it to the other words in the strs list
        #If they are not the same, shorten the prefix by one until you get someting in common
        prefix = strs[0]
        
        for word in strs[1:]:
            while prefix != word[0:len(prefix)]:
                prefix = prefix[0:len(prefix)-1]

        return prefix 
    
    
