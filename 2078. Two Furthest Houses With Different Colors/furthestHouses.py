class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        '''
        Logic - we want to check the furthest distance from houses of different colors. To do this, we
        will set up two pointers at the beginning and end of the colors list, then move the left pointer 
        inwards while it is not equal to the pointer at the end of the list. We will also move the right 
        pointer inwards until it equals the number at the beginning of the list and take the max of the two
        distances we have measured. 
        '''
        lp = 0
        rp = len(colors)-1
        
        while rp>lp:
            if colors[lp] != colors[rp]:
                output1 = rp - lp
                break
            else:
                lp += 1
                
        lp2 = 0
        rp2 = len(colors)-1
        while rp2>lp2:
            if colors[lp2] != colors[rp2]:
                output2 = rp2 - lp2
                break
            else:
                rp2 -= 1
        
        return max(output1, output2)