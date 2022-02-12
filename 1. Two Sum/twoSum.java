class Solution {
    public int[] twoSum(int[] nums, int target) {
        //Make a hashmap to store key, value pairs
        Map<Integer, Integer> seen = new HashMap();
        
        //Logic - loop throught the nums list, if we have seen a value that equals to target return the indexes
        //Otherwise, continue to build the hashmap
        for (int i = 0; i<nums.length; i++){
            int complement = target-nums[i];
            if (seen.containsKey(complement)) {
                return new int[] {seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        //Throw an error in case there is no match
        throw new IllegalArgumentException("no match");
    }
}
