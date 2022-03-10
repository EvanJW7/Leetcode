class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Set up your array of infinite numbers so you will always have a minimum without messing up a test
        my_array = [float('inf') for amount in range(amount+1)]
        #Array at index 0 is 0 because there to make an amount of 0 you need 0 coins
        my_array[0] = 0
        
        #Iterate through the coins first then the nums in your array
        for coin in coins:
            for num in range(len(my_array)):
                #If the num is greater or equal to the coin we are on, then we can start comparing
                if num >= coin:
                    #The min number of coins is equal to the min of the number of the array(prevmin) and 1+ the num-coin
                    #We add one because we are adding a coin to the equation no matter what so we must account for it
                    my_array[num] = min(my_array[num], 1+my_array[num-coin])
                    
        return my_array[amount] if my_array[amount] != float("inf") else -1
        