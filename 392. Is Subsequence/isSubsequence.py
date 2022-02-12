class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Use a two pointer approach, set both to 0
        i, j = 0, 0
        
        #While i and j are both in range...
        while i <len(s) and j<len(t):
            #If the letter at i is equal to the letter at j, increment i
            if s[i] == t[j]:
                i += 1
            #j gets incremented no matter the scenario so we don't need an else statement
            j += 1
        
        #When we get to the end, i should be equal to the length of s, otherwise no subsequence
        return i == len(s)
        
            