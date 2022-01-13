class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        if len(needle) == 0:
            return 0
        if needle in haystack:
            return haystack.index(needle)