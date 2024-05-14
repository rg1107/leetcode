class Solution {
    /**
    https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/solutions/5144610/standard-dp-tabulation-c-java-python-java-script
     */
    public int minimumSubstringsInPartition(String S) {
        int N = S.length();
        int[] DP = new int[N];
        Arrays.fill(DP,N);
        for (int END = 0 ; END < N ; END++){
            int[] charFreq = new int[26];
            for (int START = END ; START >= 0 ; START--){
                charFreq[S.charAt(START) - 'a']++;
                if (isBalanced(charFreq)){
                    DP[END] = START > 0 ? Math.min(DP[END] , 1 + DP[START - 1]) : 1;
                }
            }
        }
        return DP[N - 1];
    }

    // private int helper(int i, int n, int[] freq, String s) {
    //     if (i>=n && check(freq)) {
    //         return 0;
    //     }
        
    //     if (i>=n) {
    //         return 10000;
    //     }
        
    //     freq[s.charAt(i) - 97] ++;
    //     int ans = 10000;
        
    //     if (check(freq)) {
    //         ans = Math.min(ans, 1 + helper(i+1, n, new int[26], s));
    //     }
        
    //     ans = Math.min(ans, helper(i+1, n, freq, s));
    //     return ans;
    // }
    
    public boolean isBalanced(int[] charFreq) {
        int minFreq = 1001, maxFreq = 0;
        for (int Freq : charFreq) {
            if (Freq > 0) {
                minFreq = Math.min(minFreq , Freq);
                maxFreq = Math.max(maxFreq , Freq);
            }
        }
        return minFreq == maxFreq;
    }
}