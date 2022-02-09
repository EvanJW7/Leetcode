class Solution {
    public int[] twoSum(int[] nums, int target) {
        //Make a hashmap to store key, value pairs
        Map<Integer, Integer> seen = new HashMap<>();
        
        
        //Logic - loop throught the nums list, if we have seen a value that equals to target return the indexes
        //Otherwise, continue to build the hashmap 
        for (int i = 0; i<nums.length; i++){
            if (seen.containsKey(target - nums[i])) {
                return new int[] {seen.get(target-nums[i]), i};
            }
            seen.put(nums[i], i);
        }
        //Throw an error so you will always have a return statement 
        throw new IllegalArgumentException("no match");
    }
}
