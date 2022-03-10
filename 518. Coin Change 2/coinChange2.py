class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #Make an array starting at 0 and ending at the amount number
        ways = [0 for num in range(0, amount+1)]
        #Make the first index of ways a 1 as a base case because there is 1 way to make 0 which is to do nothing
        ways[0] = 1
        
        #Iterate through the coins and the num in our ways array
        #The algorithm is add the ways to make change with the num plus ways to make change with the num minus the coin
        for coin in coins:
            for num in range(len(ways)):
                if num >= coin:
                    ways[num] = ways[num] + ways[num-coin]
                    
        #Return the value at the last index of our array
        return ways[amount]
