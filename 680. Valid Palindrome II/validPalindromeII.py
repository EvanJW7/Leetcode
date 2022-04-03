class Solution:
    def validPalindrome(self, s: str) -> bool:
        #Initialize your left and right pointers
        lp = 0
        rp = len(s)-1
        
        #While they do not cross, check to see if the letter at each pointer is equal. If so, increment
        while lp<rp:
            if s[lp] == s[rp]:
                lp += 1
                rp -= 1
            #If the letters at both pointers are not equal, check to see if the subarray of either the 
            #left letter being skipped or the right letter being skipped is a palindrome. If yes, we
            #can return true
            else:
                skipL = s[lp + 1: rp+1]
                skipR = s[lp:rp]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
           
        return True 
            