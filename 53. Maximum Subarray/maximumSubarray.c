int maxSubArray(int* nums, int numsSize){
    //Make your two variables with max_sum equal to the first number and
    //current_sum equal to 0
    int max_sum = nums[0];
    int current_sum = 0;

    //Iterate through the nums array, use Kadane's algorithm to find the max sum 
    for (int i = 0; i<numsSize; i++){
        if(current_sum + nums[i]> nums[i]) current_sum = current_sum + nums[i];
        else
            current_sum = nums[i];
        if (max_sum < current_sum) max_sum = current_sum;
        else
            max_sum = max_sum;

}
    return max_sum;
}

