class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        #First off, we want to sort the array so we can check the differences between one to another
        arr.sort()
        #Now find the minimum difference of all the nums in arr
        mins = []
        for i in range(len(arr)-1):
            mins.append(abs(arr[i+1]-arr[i]))
        minDifference = min(mins)
        
        #Now that we have the minimum difference, go through the array and check which pair(s) have this difference
        #Append those pairs to output and return them
        output = []
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i]) == minDifference:
                output.append([arr[i], arr[i+1]])
        return output 