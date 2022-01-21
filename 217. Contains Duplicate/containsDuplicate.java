class Solution {
    public boolean containsDuplicate(int[] nums) {
        //Sort the nums array
        Arrays.sort(nums);
        //Loop through, check if i=i+1, if so, return true/return false
        for (int i = 0; i<nums.length-1; i++){
            if (nums[i] == nums[i+1]) return true;
        }
    return false;
    }
}
