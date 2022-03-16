class Solution {
    public boolean lemonadeChange(int[] bills) {
        int fives = 0;
        int tens = 0;
        
        for (int bill : bills){
            if(bill == 5){
                fives++;
            }
            else if (bill == 10 && fives>0){
                fives -= 1;
                tens += 1;
            }
            else if(bill == 20 && fives > 0 && tens > 0){
                tens -= 1;
                fives -= 1;
            }
            else if (bill == 20 && fives >= 3){
                fives -= 3;
            }
            else{
                return false;
                }
            }
            return true;
        }
    }