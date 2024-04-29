class Solution {
    /**
    https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/solutions/3111664/java-c-python-should-be-pow-2-n-4
    */
    public int monkeyMove(int n) {
        long res = 1, base = 2, mod = (long)1e9 + 7;
        while (n > 0) {
            if (n % 2 == 1)
                res = res * base % mod;
            base = base * base % mod;
            n >>= 1;
        }
        return (int)((res - 2 + mod) % mod);
    }
}