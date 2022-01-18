class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Set i at 0, use a while loop
        i = 0
        #As soon we find it's a power of two, return True
        while i < 31:
            if 2**i == n:
                return True
            #Else, increment i by one
            i += 1
        return False 
       
        