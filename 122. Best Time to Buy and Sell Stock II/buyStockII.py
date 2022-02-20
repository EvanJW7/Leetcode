class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Logic - we want to tally up the total profit from all profitable trades
        #Set an i pointer initialized to 0 and a total variable initialized to 0
        i = 0
        total = 0
        #We only need one for loop since we are comparing i with i+1
        for i in range(len(prices)-1):
            #If the price from i+1 is greater than the previous, add that amount to the total
            if prices[i] < prices[i+1]:
                total += prices[i+1]-prices[i]
                #Increment i. We don't need an else statement
                i += 1
        #Return total
        return total
                