class Solution {
    public int minimumValueSum(int[] nums, int[] andValues) {
        
        HashMap<Integer, Integer>[][] dp = new HashMap[nums.length][andValues.length];
        
        int val = recur(0, 0, nums, andValues, 131071, dp);
        
        if(val >= (int)(1e9)) return -1;
        
        return val;
    }
    
    int recur(int i, int j, int[] nums, int[] andValues, int runningAnd, HashMap<Integer, Integer>[][] dp) {

        if(i == nums.length && j == andValues.length) {
            return 0;
        }
        
        if(j == andValues.length || i == nums.length) return (int)1e9;
        

        if(dp[i][j] != null && dp[i][j].get(runningAnd) != null) return dp[i][j].get(runningAnd);
        
        int newRun = runningAnd & nums[i];
                
        int tryNew = (int)(1e9);
        if(newRun == andValues[j]) tryNew = nums[i] + recur(i + 1, j + 1, nums, andValues, 131071, dp);
        int cont = recur(i + 1, j, nums, andValues, newRun, dp);
        
        if(dp[i][j] == null) dp[i][j] = new HashMap<>();
        dp[i][j].put(runningAnd, Math.min(tryNew, cont));
        return Math.min(tryNew, cont);
    }
}