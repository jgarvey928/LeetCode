class Solution {
    public int removeDuplicates(int[] nums) {
        int[] temp = new int[nums.length];
        int i = 0;
        int total = 0;
        for(int k = 0; k < nums.length; k++){
            if(k == nums.length - 1){
                if(temp[i] != nums[nums.length - 1]){
                    temp[i] = nums[nums.length - 1];
                    total++;
                }
            }
            else if (nums[k] == nums[k+1]){
                int count = 1;
                total ++;
                int j = k+2;
                while( j < nums.length){
                    if(nums[k] == nums[j]){
                        count++;
                    }
                    j++;
                }
                temp[i] = nums[k];
                i++;
                k += count;
            }else{
                temp[i] = nums[k];
                total++;
                i++;
            }
        }
        // for(int num: temp){print(num+"");}
        for(int z = 0; z < nums.length; z++){
            if(z < total){nums[z] = temp[z];}
            else{nums[z] = 0;}
        }

        return temp.length - (temp.length-total);
    }

    public static void print(String value){ System.out.print(value);}
}