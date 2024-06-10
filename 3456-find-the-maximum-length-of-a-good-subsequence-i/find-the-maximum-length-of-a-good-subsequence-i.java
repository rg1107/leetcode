class Solution {
    /*
    https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/solutions/5280192/easy-java-beats-100-dp-take-nottake
    https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/solutions/5280180/java-c-python-dp-o-nk
    */
    public int maximumLength(int[] nums, int k) {
        Integer[][][] dp = new Integer[nums.length+1][k + 1][nums.length + 1];
        return rec(nums,k,0,-1,dp);
    }
    public int rec(int[] nums,int k,int i,int prev,Integer dp[][][]){
        if(i==nums.length)return dp[i][k][prev+1]= 0;
        if(dp[i][k][prev+1] !=null)return dp[i][k][prev+1];
        int take=0;
        if (prev == -1 || nums[prev] == nums[i]) {            
            take = 1 + rec(nums, k, i + 1, i,dp);
        } else if (k > 0) {            
            take = 1 + rec(nums, k - 1, i + 1, i,dp);
        }
        
        int ntake=rec(nums,k,i+1,prev,dp);
        return dp[i][k][prev+1]= Math.max(take,ntake);
    }

    // public int maximumLength(int[] A, int k) {
    //     Map<Integer, Integer>[] dp = new HashMap[k + 1];
    //     for (int i = 0; i <= k; i++) {
    //         dp[i] = new HashMap<>();
    //     }
    //     int[] res = new int[k + 1];
    //     for (int a : A) {
    //         for (int i = k; i >= 0; --i) {
    //             int v = dp[i].getOrDefault(a, 0);
    //             v = Math.max(v + 1, (i > 0 ? res[i - 1] + 1 : 0));
    //             dp[i].put(a, v);
    //             res[i] = Math.max(res[i], v);
    //         }
    //     }
    //     return res[k];
    // }
}