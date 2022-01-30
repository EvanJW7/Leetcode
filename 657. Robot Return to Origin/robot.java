class Solution {
    public boolean judgeCircle(String moves) {
        //Initialize int variables x and y to 0
        int x = 0;
        int y = 0;
        //Loop through the moves string and add or subract from x and y
        for(char move : moves.toCharArray()){
            if (move == 'U'){
                y += 1;
            }
            else if (move == 'D'){
                y -= 1;
            }
            else if (move == 'R'){
                x += 1;
            }
            else{
                x-=1;
            }
            
        }
        //Return a boolean if x and y are both equal to 0
        return (x == 0 && y == 0);
    }
}
    