public class Solution {
    public int MaxProfit(int[] prices) {
        int currentMax = 0;
        int buy = 0;
        int sell = 1;

        while (sell < prices.Length) {
            if (prices[buy] < prices[sell]) {
                int profit = prices[sell] - prices[buy];
                currentMax = Math.Max(profit, currentMax);
            } else {
                buy = sell;
            }
            sell++;
        }

        return currentMax;
    }
}
