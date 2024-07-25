class Solution {
    /**
    https://leetcode.com/problems/longest-common-subsequence/solutions/348884/c-with-picture-o-nm
     */
    public int longestCommonSubsequence(String a, String b) {
        int[][] m = new int[1001][1001];
        for (int i = 0; i < a.length(); ++i)
            for (int j = 0; j < b.length(); ++j)
                m[i + 1][j + 1] = a.charAt(i) == b.charAt(j) ? m[i][j] + 1 : Math.max(m[i + 1][j], m[i][j + 1]);
        return m[a.length()][b.length()];   
    }
}