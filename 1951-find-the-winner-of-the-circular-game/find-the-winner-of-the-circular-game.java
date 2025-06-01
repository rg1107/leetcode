class Solution {
    /**
    https://leetcode.com/problems/find-the-winner-of-the-circular-game/solutions/5438775/explanations-no-one-will-give-you-3-detailed-approaches-extremely-simple-and-effective
     */
    public int findTheWinner(int n, int k) {
        return recursion(n, k) + 1;
    }

    private int recursion(int n, int k) {
        if (n == 1) {
            return 0;
        }
        return (recursion(n - 1, k) + k) % n;
    }
}