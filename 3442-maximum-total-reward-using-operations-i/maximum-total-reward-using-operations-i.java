class Solution {
    public int maxTotalReward(int[] rewardValues) {
        // In case of duplicate values, we can select only one of them at any time, so removing duplicates while calculating.
        Set<Integer> set = new HashSet<>();
        int max = 0;
        for (int num : rewardValues) {
            set.add(num);
            max = Math.max(num, max);
        }
        
        List<Integer> list = set.stream().collect(Collectors.toList());
        Collections.sort(list);
        int n = list.size();
        int[][] dp = new int[n][2*max+1];
        for (int i=0;i<n;i++) {
            Arrays.fill(dp[i], -1);
        }
        
        helper(0, 0, list, n, dp);
        return dp[0][0];
    }
    
    public int helper(int curr, int ind, List<Integer> rewards, int n, int[][] dp) {
        if (ind >= n) {
            return curr;
        }
        
        if (dp[ind][curr] != -1) {
            return dp[ind][curr];
        }
        
        // To select or not to select is the choice here.
        if (curr < rewards.get(ind)) {
            dp[ind][curr] = Math.max(helper(curr + rewards.get(ind), ind + 1, rewards, n, dp), dp[ind][curr]);
            //max = Math.max(helper(curr + rewards.get(ind), ind + 1, rewards, n, dp), max);
        }
        
        dp[ind][curr] = Math.max(helper(curr, ind + 1, rewards, n, dp), dp[ind][curr]);
        //max = Math.max(helper(curr, ind + 1, rewards, n, dp), max);
        
        return dp[ind][curr];
    }
}