class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Initialize two pointers set to 0 and 1 and set a maxProfit variable set to 0
        lp = 0
        rp = 1
        maxProfit = 0
        
        #While the right pointer is less than the length of prices
        while rp<len(prices):
            '''
            Logic - we are basically finding a low and checking the max profit it can make until the end 
            of the array. If we find a new low, we update the left pointer and continue to check maxProfit
            '''
            #If the trade is profitable, check it against the max profit and update if needed
            if prices[lp] < prices[rp]:
                maxProfit = max(maxProfit, prices[rp]-prices[lp])
            #If the trade is not profitable, reset the left pointer to where the right pointer was
            else:
                lp = rp
            #Increment the right pointer no matter what
            rp += 1
            
        return maxProfit 
