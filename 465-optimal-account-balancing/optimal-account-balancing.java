class Solution {
    /**
    https://leetcode.com/problems/optimal-account-balancing/solutions/1157154/java-clean-backtracking-solution-with-comments
     */
    public int minTransfers(int[][] transactions) {
        // Key: person's ID   Value: person's balence after calculation
        // {1 : -5} means person 1 should get $5
        // {2 : 10} means person 2 should pay $10
        Map<Integer, Integer> map = new HashMap<>();
        for (int[] trans : transactions) {
            map.put(trans[0], map.getOrDefault(trans[0], 0) - trans[2]);
            map.put(trans[1], map.getOrDefault(trans[1], 0) + trans[2]);
        }
        
        // Since after we get those amount of balence, person's ID does not affect the final result
        int n = map.size(), i = 0;
        int[] balance = new int[n];
        for (int k : map.keySet()) {
            balance[i++] = map.get(k);
        }
        
        return dfs(0, balance);
    }
    
    private int dfs(int idx, int[] balance) {
        if (idx == balance.length) return 0;                  // all balence are cleared ==> requires 0 operation
        if (balance[idx] == 0) return dfs(idx + 1, balance);  // curr person has balence 0 ==> skip curr person
        
        int res = Integer.MAX_VALUE;
        
        int currDebt = balance[idx];
        
        for (int i = idx+1; i < balance.length; i++) {
            /* Key step 1 :
                if either 1. balence[idx] & balence[i] are both positive or negative 
                          2. balence[idx] | balence[i] has 0 balance 
                then operate between them is meaningless 
            */
            if (balance[i] * currDebt >= 0) continue;
            
            /* Key Step 2 : 
                transfer all balance from balance[idx] to balance[i], i.e., 
                after the transaction, balance[idx] = 0
          
            */
            balance[i] += currDebt;
            res = Math.min(res, 1 + dfs(idx + 1, balance));
            balance[i] -= currDebt;   
            
            
        }
        return res;
    }
}