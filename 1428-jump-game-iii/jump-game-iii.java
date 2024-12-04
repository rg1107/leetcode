class Solution {
    /**
    https://leetcode.com/problems/jump-game-iii/solutions/465602/java-c-python-1-line-recursion
     */
    public boolean canReach(int[] A, int i) {
        //Sign is flipped to mark the node as visited.
        return 0 <= i && i < A.length && A[i] >= 0 && ((A[i] = -A[i]) == 0 || canReach(A, i + A[i]) || canReach(A, i - A[i]));
    }
}