class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #All we need to do here is sort the two strings alphabetically and then compare them
        t = "".join(sorted(t))
        s = "".join(sorted(s))
        
        return s == t