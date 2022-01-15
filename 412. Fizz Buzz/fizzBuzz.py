class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #Make empty list
        output = []
        #Iterate over each num in range 1, n+1
        for num in range(1, n+1):
            if num%3 == 0 and num%5 == 0:
                output.append("FizzBuzz")
            elif num%3 == 0:
                output.append("Fizz")
            elif num%5 == 0:
                output.append("Buzz")
            #Important: appending str(num) in one step speeds things up
            else:
                output.append(str(num))
        return output 