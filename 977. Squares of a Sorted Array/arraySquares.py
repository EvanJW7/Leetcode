class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Use a two pointer approach here for optimal run time
        lp = 0
        rp = len(nums)-1
        #Make an empty output array
        output = []
        #While the pointers at both ends do not cross, compare the numbers and append to the larger on to output
        while lp <= rp:
            if abs(nums[lp]) > nums[rp]:
                output.append(nums[lp]*nums[lp])
                lp += 1
            else:
                output.append(nums[rp]*nums[rp])
                rp -= 1
        #Return the output array reversed since it it not in the correct order when we simply append it    
        return output[::-1]
        