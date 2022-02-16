class Solution:
    def reverseVowels(self, s: str) -> str:
        #Use a two pointer approach to compare and switch the vowels
        lp = 0
        rp = len(s)-1
        s = list(s)
        vowels = 'aeiouAEIOU'
        
        #While the left pointer is less than the right pointer, iterate and check if the letter is a vowel
        while lp < rp:
            #If the letter is not a vowel, incremenet lp and decremenet rp
            if s[lp] not in vowels:
                lp += 1
            elif s[rp] not in vowels:
                rp -= 1
            #If both indexes are vowels, switch them. Make sure to increment/decrement 
            elif s[lp] in vowels and s[rp] in vowels:
                s[rp], s[lp] = s[lp], s[rp]
                lp += 1
                rp -= 1
                
        #Put s back into a string form and return it     
        output = ""
        for letter in s:
            output += letter
        return output
        