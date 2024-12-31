public class Solution {
    private static final int MOD = 1000000007;
    public long power(long x, long y) {
            long result = 1;
            x = x % MOD;
            while (y > 0) {
                if (y % 2 == 1) {
                    result = (result * x) % MOD;
                }
                x = (x * x) % MOD;
                y = y / 2;
            }
            return result;
        }
    public long modInverse(long a) {
            return power(a, MOD - 2);
        }
    public long nCr(long n, long r) {
            if (r > n || n < 0 || r < 0) return 0;
            if (r == 0) return 1;

            long num = 1;
            long den = 1;

            for (long i = 0; i < r; i++) {
                num = (num * (n - i)) % MOD;
                den = (den * (i + 1)) % MOD;
            }
            return (num * modInverse(den)) % MOD;
        }
    public int countGoodArrays(int n, int m, int k) {
        if(n==1&&m==1&&k==0)return 1;
        if (n <= 0 || m <= 0) return 0;
        if (k >= n) return 0;
        if (k < 0 || m < 1) return 0;
        long kpos = nCr(n - 1, k);
        long rem = power(m - 1, n - k - 1);
        if (rem < 0 || kpos < 0) return 0;
        long ans = (kpos * m) % MOD;
        ans = (ans * rem) % MOD;
        return (int) (ans % MOD);
    }
}