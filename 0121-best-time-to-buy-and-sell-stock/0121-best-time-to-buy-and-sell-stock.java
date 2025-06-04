class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int size = prices.length;
        int max_diff = 0;
        for(int i = 0; i < size; i++){
            for(int j = i+1; j < size; j++){
                if(prices[j] > min){
                    if(prices[j] - min > max_diff){
                        max_diff = prices[j] - min;
                    }
                }else{
                    min = prices[j];
                    i = j - 1;
                    break;
                }
            }
        }
        return max_diff;
    }
}