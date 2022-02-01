class Solution {
    public int maxProfit(int[] prices) {
        
        int res = 0;
        int[] min = new int[prices.length];
        int[] max = new int[prices.length];
        min[0] = prices[0];
        max[prices.length-1] = prices[prices.length-1];
        
        for(int i=1;i<prices.length;i++) {
            min[i] = Math.min(min[i-1], prices[i]);
        }
        
        for(int i=prices.length-2;i>=0;i--) {
            max[i] = Math.max(max[i+1], prices[i]);
        }
        
        for(int i = 0;i<prices.length;i++) {
            res = Math.max(max[i]-min[i], res);
        }
        
        return res>0?res:0;
        
    }
}