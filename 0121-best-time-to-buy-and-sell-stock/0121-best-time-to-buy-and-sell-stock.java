class Solution {
    public int maxProfit(int[] prices) {
        // Initialize the minimum price to a very high value
        int minPrice = Integer.MAX_VALUE;
        // Initialize the maximum profit to 0
        int maxProfit = 0;
        
        for (int i = 0; i < prices.length; i++) {
            // Update minPrice if the current price is lower
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            } 
            // Calculate profit if sold today and update maxProfit if it's higher
            else if (prices[i] - minPrice > maxProfit) {
                maxProfit = prices[i] - minPrice;
            }
        }
        
        return maxProfit;
    }
}