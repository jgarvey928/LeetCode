class Solution {
    public int[] runningSum(int[] nums) {
        // Start from the second element (index 1)
        for (int i = 1; i < nums.length; i++) {
            // The current element becomes the sum of itself and the previous running sum
            nums[i] += nums[i - 1];
        }
        return nums;
    }
}