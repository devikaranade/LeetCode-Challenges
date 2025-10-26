class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int left=0;
        int right=0;

        while (right<prices.length){
            int diff = prices[right]-prices[left];
            if (diff>max_profit){
                max_profit=diff;
            }
            if (diff<0) {
                left=right;
            }
            right++;
        }
        return max_profit;

    }
}