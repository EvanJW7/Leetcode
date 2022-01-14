class Solution:
    def mySqrt(self, x: int) -> int:
        #Simply use the math sqrt function to return the correct answer. Must be an int because the default is a float 
        import math
        return int(math.sqrt(x))
        