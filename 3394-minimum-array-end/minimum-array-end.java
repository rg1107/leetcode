class Solution {
    /**
    https://leetcode.com/problems/minimum-array-end/solutions/5081947/java-c-python-bits-manipulation
     */
    public long minEnd(int n, int x) {
        // long a = x;
        // while (--n > 0)
        //     a = (a + 1) | x;
        // return a;

        n--;
        long a = x;
        for (long b = 1; n > 0; b <<= 1) {
            if ((b & x) == 0) {
                a |= (n & 1) * b;
                n >>= 1;
            }
        }
        return a;
    }
}