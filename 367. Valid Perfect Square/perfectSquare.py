class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        This is a binary search algorithm. It is much faster than looping through every num
        in the range of 1 and 2^31-1. We can easily eliminate large blocks of nums with this approach
        '''
        left = 0
        right = num
        
        #While the pointers do not cross
        while left <= right:
            #Calculate mid pointer based on left and right
            mid = left + (right-left)//2
            #If the mid squared is equal to the num, we have a perfect square. Return true
            if  mid ** 2 == num:
                return True
            #If the mid squared is greater than the num, move the right pointer to one less than the mid
            elif mid ** 2 > num:
                right = mid -1
            #If the mid squared is less than the num, move the left pointer to one more than the mid
            elif mid ** 2 < num:
                left = mid +1
        #If there is no perfect square, eventually we will break the loop and return False 
        return False