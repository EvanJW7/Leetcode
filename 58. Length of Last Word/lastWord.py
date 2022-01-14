class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #Split the string and return len of the -1 index 
        return len(s.split()[-1])
        
    