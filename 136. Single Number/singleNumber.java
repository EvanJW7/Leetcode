class Solution {
    public int singleNumber(int[] nums) {
        
        int result = 0;
        //We can use BitOr to find the number than appears only once
        for (int i = 0; i<nums.length; i++){
            result = result ^ nums[i];
        }
        return result;
    }
}