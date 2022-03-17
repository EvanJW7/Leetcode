class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        Logic - this is a dynamic programming problem. We want to loop through the list and 
        add minimum of i - 1 and i - 2 to the current iteration as that will account for the 
        minimum cost it takes to get to each position. Then we can return the minimum of the 
        last two indexes in the cost array. Another way to solve this is to create a new array
        that we append to but modifying the original array in place works well too. 
        '''
        j = len(cost)
        
        for i in range(2, j):
            cost[i] += min(cost[i-1], cost[i-2])
        
        return min(cost[-1], cost[-2])