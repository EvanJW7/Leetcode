class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Logic - since the numbers list is sorted, set up a pointer at 0 and at the end of the list. If the numbers
        at indexes lp and rp are greater than the target, then decrease the total by decrementing the right pointer 
        and try again. If the numbers at indexes lp and rp are less than the total, we increment the left pointer
        to get a larger total. Do this back and forth until we get a solution since a solution is guaranteed. 
        '''
        lp = 0
        rp = len(numbers)-1
        
        while numbers[lp] + numbers[rp] != target:
            if numbers[lp] + numbers[rp] > target:
                rp -= 1
            elif numbers[lp] + numbers[rp] < target:
                lp += 1

        return [lp+1, rp+1]