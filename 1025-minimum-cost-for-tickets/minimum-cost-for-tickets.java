class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        // int[] minCosts = new int[days.length];
        // Arrays.fill(minCosts, Integer.MAX_VALUE);
        // helper(0, days, costs, minCosts, 0);
        // return minCosts[0];

        boolean[] isTravelDay = new boolean[366];
        for (int day : days) {
            isTravelDay[day] = true;
        }
        int[] dp = new int[366];
        for (int i = 1; i < 366; i++) {
            if (!isTravelDay[i]) {
                dp[i] = dp[i - 1];
                continue;
            }
            dp[i] = Integer.MAX_VALUE;
            dp[i] = Math.min(dp[i], dp[Math.max(0, i - 1)] + costs[0]);
            dp[i] = Math.min(dp[i], dp[Math.max(0, i - 7)] + costs[1]);
            dp[i] = Math.min(dp[i], dp[Math.max(0, i - 30)] + costs[2]);
        }
        return dp[365];
        
    }

    private int helper(int index, int[] days, int[] costs, int[] minCosts, int total) {
        if (index >= days.length) {
            return total;
        }

        if (minCosts[index] != Integer.MAX_VALUE) {
            return minCosts[index];
        }

        int cost1 = helper(index + 1, days, costs, minCosts, total + costs[0]);
        int sIndex = index;
        int tIndex = index;
        
        while (sIndex < days.length && days[sIndex] < days[index] + 7) {
            sIndex++;
        }

        while (tIndex < days.length && days[tIndex] < days[index] + 30) {
            tIndex++;
        }

        int cost2 = helper(sIndex, days, costs, minCosts, total + costs[1]);
        int cost3 = helper(tIndex, days, costs, minCosts, total + costs[2]);

        minCosts[index] =  Math.min(cost1, Math.min(cost2, cost3));
        return minCosts[index];
    }
}