class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Make a new array with the same elements of the old array
        myarr = arr
        i = 0
        j = 1
        #Iterate through the list, and change the variable at the i index to the max of j to the end
        while i < len(arr)-1:
            myarr[i] = max(arr[j:])
            i += 1
            j += 1
        #Make sure to make the last index -1
        myarr[-1] = -1
        return myarr