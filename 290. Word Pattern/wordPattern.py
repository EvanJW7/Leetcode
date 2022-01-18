class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #Split s
        s = s.split()
        #Take care of edge case. If lengths are different, pattern will be false
        if len(s) != len(pattern):
            return False 
        #Make empty dictionary to compare
        matches = {}
        #Iterate starting at 0
        i = 0
        while i<len(s):
            #If letter in pattern not in dictionary, add it. Letter:Word
            if pattern[i] not in matches:
                #If the letter in values already, return False
                if s[i] in matches.values():
                    return False
                matches[pattern[i]] = s[i]
            else:
                #If the letter does not equal the word from the dictionary, return False
                if matches[pattern[i]] != s[i]:
                    return False 
            #After going though all possible scenarios, increment i by 1
            i+=1
            
        return True 
            