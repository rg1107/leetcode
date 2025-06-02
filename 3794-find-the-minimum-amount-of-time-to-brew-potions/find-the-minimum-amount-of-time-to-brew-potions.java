class Solution {
    /**
    https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/solutions/6568728/java-c-python-prefix-sum
     */
    public long minTime(int[] skill, int[] mana) {
        int n = skill.length, m = mana.length;
        long[] acc = new long[n + 1];
        for (int i = 0; i < n; i++) {
            acc[i + 1] = acc[i] + skill[i];
        }
        long t = 0, t2 = 0;
        for (int j = 1; j < m; j++) {
            t2 = 0;
            for (int i = 0; i < n; i++) {
                t2 = Math.max(t2, t + mana[j - 1] * acc[i + 1] - mana[j] * acc[i]);
            }
            t = t2;
        }
        return t + mana[m - 1] * acc[n];
    }
}