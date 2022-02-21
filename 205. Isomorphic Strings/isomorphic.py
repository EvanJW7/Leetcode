class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #Take care of edge case to speed up run time
        #If the two strings are not the same length, they will not be isomorphic  
        if len(s) != len(t):
            return False
        
        #Make an empty dictionary to keep track of the letters we have seen already 
        seen = {}
        
        #Iterate through the letters in s
        for i, letter in enumerate(s):
            #If the letter is not in the seen dict and the letter in t is already in there, return False right away
            if letter not in seen and t[i] in seen.values():
                return False
            #If the letter in both s and t are not in the dictionary, add them
            elif letter not in seen:
                seen[s[i]] = t[i]
            #If the letter in s is already in seen with another pairing, return False
            elif letter in seen and seen[s[i]] != t[i]:
                return False 
        #If we get through all those scenarios with a dictionary that meets our standards, we have isomorphic strings 
        return True 
        