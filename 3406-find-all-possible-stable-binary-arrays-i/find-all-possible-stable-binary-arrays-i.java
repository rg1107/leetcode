class Solution {
    /**
    https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/solutions/5080179/java-dynamic-programming
     */
    private static final int MOD = (int) (1e9 + 7);
    
    private int countStableArrays(int zeroes, int ones, int prev, int prevCount, int limit, Integer[][][][] dp) {
        if (zeroes == 0 && ones == 0) {
            return 1;
        }
        
        if (dp[zeroes][ones][prev][prevCount] != null) {
            return dp[zeroes][ones][prev][prevCount];
        }
        
        int countHere = 0;
        if (zeroes > 0) {
            if (prev != 0 || prevCount + 1 <= limit) {
                countHere = countStableArrays(zeroes - 1, ones, 0,
                                    prev == 0 ? prevCount + 1 : 1, limit, dp) % MOD;
            }
        }
        
        if (ones > 0) {
            if (prev != 1 || prevCount + 1 <= limit) {
                countHere = (countHere + countStableArrays(zeroes, ones - 1, 1,
                                    prev == 1 ? prevCount + 1 : 1, limit, dp)) % MOD;
            }
        }
        return dp[zeroes][ones][prev][prevCount] = countHere;
    }
    
    public int numberOfStableArrays(int zero, int one, int limit) {
        Integer[][][][] dp = new Integer[zero + 1][one + 1][3][limit + 1];
        return countStableArrays(zero, one, 2, 0, limit, dp);
    }
}