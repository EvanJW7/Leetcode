class Solution:
    def decodeString(self, s: str) -> str:
        mystack = []
        for i in range(len(s)):
            if s[i] != ']':
                #Until we see a closing bracket, add chars to our stack
                mystack.append(s[i])
            #Once we hit a closing bracket, gather the letters in the brackets
            else:
                mystring = ""
                while mystack[-1] != '[':
                    #gather the letters into a string
                    mystring = mystack.pop() + mystring
                #Pop off the opening bracket
                mystack.pop()
                
                #Now we multiply our string with the number that came before the first bracket
                nums = ""
                while mystack and mystack[-1].isdigit():
                    nums = mystack.pop() + nums
                #Now we append our result to the stack and continue where we left off in the loop
                mystack.append(int(nums)*mystring)
                
        #Return the stack in string format
        return "".join(mystack)