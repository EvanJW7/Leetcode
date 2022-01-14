class Solution:
    def isValid(self, s: str) -> bool:
        #Make an empty stack, lookup dictionary to be able to reference the parenthesis 
        stack = []
        lookup = {')':'(', '}':'{', ']':'['}
        #If the length of s is only 1, the output is automatically false
        if len(s) == 1:
            return False 
        
        #Go through each parenthesis in s and check if it's in lookup
        for p in s:
            #If it's in lookup, add it to the stack
            if p in lookup.values():
                stack.append(p)
            #If the parenthesis is not in lookup.values, then it is a closing parenthesis.
            #Check if the opposite parenthesis is the last value in the stack.
            #The stack must be non empty at this point, and if it's not, it should return false 
            elif len(stack) > 0 and lookup[p] == stack[-1]:
                stack.pop()
            else:
                return False
        #Return a boolean whether or not the stack is empty 
        return stack == []
        