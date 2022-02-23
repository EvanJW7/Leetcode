class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        Logic - create a frequency dictionary of the letters in magazine, then
        check each whether each letter from ransomNote is in the dictionary. If it's 
        not, return false. If it is, great, decrease the frequency by one.  If we 
        ever see a frequency of less than 0, we can return false since there are not 
        enough letters in magazine to account for the letters in ransomNote
        '''
        magFreq = {}
        for letter in magazine:
            if letter not in magFreq:
                magFreq[letter] = 1
            else:
                magFreq[letter] += 1
        for letter in ransomNote:
            if letter in magFreq:
                magFreq[letter] -= 1
                if magFreq[letter] < 0:
                    return False
            if letter not in magFreq:
                return False 
        return True 