class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #Make empty list
        output = []
        #Iterate over each num in range 1, n+1
        #To speed up run time, start off saying if num%15 instead of %3 and %5.
        for num in range(1, n+1):
            if num%15 == 0:
                output.append("FizzBuzz")
            elif num%3 == 0:
                output.append("Fizz")
            elif num%5 == 0:
                output.append("Buzz")
            #Important: appending str(num) in one step speeds things up
            else:
                output.append(str(num))
        return output 
