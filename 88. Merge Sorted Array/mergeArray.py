class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #Make a last index variable so you can fill in from back to front
        last_index = m + n -1
        
        #While m and n are both greater than 0, traverse and fill in with the larger number
        while m > 0 and n > 0:
            if nums1[m-1]<nums2[n-1]:
                nums1[last_index] = nums2[n-1]
                n -= 1
              
            else:
                nums1[last_index] = nums1[m-1]
                m -= 1
            last_index -= 1
            
        #If n gets to 0 before m, we are done. However, if m gets to 0 before n, there is more to do. 
        #While n > 0, fill nums1 with the numbers of nums2
        while n > 0:
            nums1[last_index] = nums2[n-1]
            n -= 1
            last_index -= 1