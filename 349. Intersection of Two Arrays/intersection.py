class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #All we have to do is compare the two lists and take a set of shared numbers
        #To use the & operator we must turn the lists into sets. 
        x = set(nums1) & set(nums2)
        #Now we can return a list of the output 
        return list(x)