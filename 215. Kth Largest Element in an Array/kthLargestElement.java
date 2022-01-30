class Solution {
    public int findKthLargest(int[] nums, int k) {
        //Since the array can contain duplicates, all we need to do
        //is sort the nums array and return the index of the kth element
        Arrays.sort(nums);
        return nums[nums.length -k];
        
    }
}
