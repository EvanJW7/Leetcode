class Solution {
    public int[] runningSum(int[] nums) {
        //Make a new integer array
        int[] myarray = new int[nums.length];
        //The sum is the first number in the nums array
        int sum = nums[0];
        myarray[0] = nums[0];
        //Add the first element to your list, then iterate through and update the sum
        for (int i = 1; i<nums.length; i++){
            sum += nums[i];
            myarray[i] = sum;
            
        }
        return myarray;
    }
     
}