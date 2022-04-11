class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #Sort the expected heights
        expected = sorted(heights)
        
        x = 0
        output = 0
        #Then compare the two, incrementing output of they do not match
        while x in range(len(heights)):
            if heights[x]!= expected[x]:
                output += 1
        #Make sure to keep x moving so you don't have an infinite loop
            x += 1
        return output 