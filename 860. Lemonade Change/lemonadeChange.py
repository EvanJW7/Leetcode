class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''
        Logic - we solve this problem by keeping track of the counts of 5 and 10. If we come across a 
        scenario when we loop through the bills where we cannot make change for the bill, we return False,
        otherwise if we get through the entire loop we can return True. We do not keep track of the number 
        of 20s because you cannot make change with a 20. This solution is O(n) time and O(1) space 
        '''
        five = 0
        ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10 and five:
            #Saying 'and five' is a short way of saying there is a number in five/five is greater than 0
                ten += 1
                five -= 1
            elif bill == 20 and ten and five:
                ten -= 1
                five -= 1
            elif bill == 20 and five>=3:
                five -= 3
            else:
                return False 
            
        return True 