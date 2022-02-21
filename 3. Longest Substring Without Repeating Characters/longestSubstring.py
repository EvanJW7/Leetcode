class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''Logic - make an empty list, then go through each letter in s and check if it is in the list. 
        If it is not, we add it. If it is, we remove the first occurance of it from the beginning and remove any numbers 
        that came before it. Then we keep track of the max length of the seen list and return it at the end
        '''
        seen = []
        maxLen = 0
        for letter in s:
            if letter not in seen:
                seen.append(letter)
            elif letter in seen:
                #In case the letter we want to remove is not the first letter in our array we need a while loop here
                while letter in seen:
                    seen.pop(0)
                seen.append(letter)
            maxLen = max(maxLen, len(seen))
            
        return maxLen
