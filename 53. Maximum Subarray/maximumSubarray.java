class Solution {
    public int maxSubArray(int[] nums) {
        //Make your two variables max_sum and current_sum
        int max_sum = nums[0];
        //Max sum has to be the first number in the array, not 0, because what would happen if they array is a singular negative number?
        //Current sum can 0 or anything below that
        int current_sum = 0;
        
        //Iterate through the nums array, use Kadane's algorithm to find the max sum 
        for(int i = 0; i<nums.length; i++){
            current_sum = Math.max(current_sum + nums[i], nums[i]);
            max_sum = Math.max(current_sum, max_sum);
        }
        
        return max_sum;
        
    }
}
