class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        '''
        Logic - make a frequency dictionary of every letter we see in sentence. 
        Return a boolean if the length of the dictionary is 26.
        '''
        seen = {}
        for letter in sentence:
            if letter not in seen:
                seen[letter] = 1
            else:
                seen[letter] += 1
        return len(seen) == 26
    