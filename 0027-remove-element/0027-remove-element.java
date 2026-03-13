class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0; // Pointer for the next position of a non-val element
        
        for (int i = 0; i < nums.length; i++) {
            // If the current element is not the value to remove
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }
        
        return k; // k is the count of elements not equal to val
    }
}