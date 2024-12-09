class Solution {
    /**
    https://leetcode.com/problems/sum-of-good-subsequences/solutions/6028686/java-c-python-dp
     */
    public int sumOfGoodSubsequences(int[] A) {
        long[] count = new long[100010];
        long[] total = new long[100010];
        long mod = 1000000007, res = 0;
        for (int a : A) {
            count[a + 1] = (count[a] + count[a + 1] + count[a + 2] + 1) % mod;
            long cur = total[a] + total[a + 2] + 1l * a * (count[a] + count[a + 2] + 1);
            total[a + 1] = (total[a + 1] + cur) % mod;
            res = (res + cur) % mod;
        }
        return (int)res;
    }
}