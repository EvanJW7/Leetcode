class Solution:
    def arrangeCoins(self, n: int) -> int:
        #Inialize variables to keep track of what we need. 
        #Total will be total coins, totalRows is total complete rows, and x is number of coins per row.
        total = 0
        totalRows = 0
        x = 0
        
        while total <= n:
            #Increment increase number of coins per row by one and add it to the total
            x = x+1
            total += x
            #Now we need to say if the total is less than or equal to n we can increments totalRows. 
            #If not, we do not have a complete row. 
            if total <= n:
                totalRows += 1
                
        #Now we can just return totalRows 
        return totalRows
            