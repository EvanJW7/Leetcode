#Solution 1
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        num = list(num)
        lp = 0
        while lp <= len(num)-1:
            if num[lp] == '9':
                lp += 1
            else:
                num[lp] = '9'
                return int("".join(num))
                
        return int("".join(num))
    
#Solution 2, one-liner
class Solution:
    def maximum69Number (self, num: int) -> int:
        return str(num).replace('6', '9', 1)