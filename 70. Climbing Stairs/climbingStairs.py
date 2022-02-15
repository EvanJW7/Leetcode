class Solution:
    def climbStairs(self, n: int) -> int:
        #If n is 2 or less, return n. The number of steps is the same as the number
        if n <= 2:
            return n
        
        #We could do this recursively, but it would take too much time.
        #Instead, set two variables equal to 1 and 2 and loop through the remaining range of steps
        #Add together the current total and return the final number
        prev = 1
        prev2 = 2
        for i in range(2, n):
            current = prev+prev2
            prev = prev2
            prev2 = current
        return current
            