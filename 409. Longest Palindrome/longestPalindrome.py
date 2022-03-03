class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        Logic- go through the s string, figure out the counts of letters than can be grouped into twos 
        and add two to the total count while removing the letter from the seen array. If a letter cannot 
        be paired with another of the same type, it will be left in the seen array. At the end of the 
        iterations, add 1 to the total count as there can be one letter with a count of one in a palindrome.
        '''
        seen = []
        count = 0
        for letter in s:
            if letter in seen:
                seen.remove(letter)
                count += 2
            else:
                seen.append(letter)
                
        #If there are letters in seen: add one to the count, if not, just return count
        if seen:
            count += 1
        return count 