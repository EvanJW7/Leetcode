class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #Use a two pointer approach to switch the letters in place
        lp = 0
        rp = len(s)-1
        #While lp is less than rp: switch the letters. Make sure to increment/decrement
        while lp<rp:
            s[rp], s[lp] = s[lp], s[rp]
            lp += 1
            rp -= 1