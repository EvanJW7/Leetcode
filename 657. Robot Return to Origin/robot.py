class Solution:
    def judgeCircle(self, moves: str) -> bool:
        #Set x and y to 0
        x = 0
        y = 0
        #Iterate through moves and add or subract from x and y
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'R':
                x += 1
            else:
                x -= 1
        #Return a boolean if x and y are both 0
        return x==0 and y==0
            
        