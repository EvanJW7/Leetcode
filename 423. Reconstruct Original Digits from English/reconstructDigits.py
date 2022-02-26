class Solution:
    def originalDigits(self, s: str) -> str:
        '''
        We want to figure out which digits have unique characters.
        If the digit does not have unique chars, figure out how to find the count 
        by subtracting the counts of other numbers that share the second most common char
        '''
        #zero -> z
        #one -> o - 0 - 2 - 4 
        #two -> w
        #three -> h - 8
        #four -> u
        #five -> f - 4
        #six -> x
        #seven -> v - 5
        #eight -> h
        #nine -> i = 8 - 6 - 5
        
        #Make a counter object and a dictionary to put in the counts of each number 1 to 9
        count = Counter(s)
        ans = {}
        
        #Nums with unique chars
        ans[0] = count['z']
        ans[2] = count['w']
        ans[4] = count['u']
        ans[6] = count['x']
        ans[8] = count['g']
        
        #Non unique num chars
        ans[3] = count['h'] - ans[8]
        ans[5] = count['f'] - ans[4]
        ans[7] = count['v'] - ans[5]
        ans[9] = count['i'] - ans[8] - ans[6] - ans[5]
        ans[1] = count['o'] - ans[0] - ans[2] - ans[4]
        
        #We now have the dictionary of the counts of each number in our given s string
        #All we need to do is return the output in string form 
        output = ""
        for i in range(10):
            if ans[i] > 0:
                output += str(i) * ans[i]
                #This makes sure if we have more than one number present it multiplies it by the count
        
        return output 
        