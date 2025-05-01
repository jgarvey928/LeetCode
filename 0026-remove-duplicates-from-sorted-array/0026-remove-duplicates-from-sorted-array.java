class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 0;
        int temp = 0;

        for(int i = 0; i < nums.length; i++) {
            if(i == 0) {
                temp = nums[i];
                count++;
            } else {
                if(temp != nums[i]) {
                    temp = nums[i];
                    nums[count] = temp;
                    count++;
                }
            }
        }

        //System.out.println(Arrays.toString(nums));
        //System.out.println(count);

        return count;
    }
}