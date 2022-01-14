class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Make an empty list
        myList = []
        #Check each letter of s, if it's alphanumeric, add the lowercase version to myList
        for letter in s:
            if letter.isalnum():
                myList.append(letter.lower())
        #Check if the new list is the same forwards and backwards, if so, True 
        if myList[::] == myList[::-1]:
            return True 
        return False 
        
    
        
                
        