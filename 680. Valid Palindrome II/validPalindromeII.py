class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::] == s[::-1]:
            return True 
        else:
            if len(s)%2 != 0 and s[::] != s[::-1]:
                 return False 
            if len(s)%2 == 0:
                one_counts = []
                for letter in s:
                    if s.count(letter) == 1:
                        one_counts.append(letter)
                        s = s.replace(letter, '')
                        if s[::] == s[::-1]:
                            return True 
                        return False 
            