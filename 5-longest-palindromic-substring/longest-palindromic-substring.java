class Solution {
    public String longestPalindrome(String s) {
        if (s.length() <= 1) {
            return s;
        }

        StringBuilder sb = new StringBuilder("#");
        for (int i =0;i<s.length();i++) {
            sb.append(s.charAt(i)).append("#");
        }
        String temp = sb.toString();
        int n = temp.length();
        int[] z = new int[n];

        int left = 0;
        int right = 0;

        for (int i = 1; i<n;i++) {
            z[i] =  i < right ? Math.min(right-i, z[left + (right-i)]) : 0;
            while (i + z[i] + 1 < n && i - z[i] - 1 >=0 && 
                    temp.charAt(i + z[i] + 1) == temp.charAt(i - z[i] - 1)) {
                z[i]++;
            }
            if ( i + z[i] > right ) {
                left =  i - z[i];
                right = i + z[i];
            }
        }

        int res = 1;
        int index = 0;
        for (int i = 0;i<n;i++) {
            if (res < z[i]) {
                res = z[i];
                index = (i - z[i])/2;
            }
        }

        return s.substring(index, index + res);
        
    }

    // public String longestPalindrome(String s) {
    //     if (s.length() <= 1) {
    //         return s;
    //     }

    //     int maxLen = 1;
    //     String maxStr = s.substring(0, 1);
    //     s = "#" + s.replaceAll("", "#") + "#";
    //     int[] dp = new int[s.length()];
    //     int center = 0;
    //     int right = 0;

    //     for (int i = 0; i < s.length(); i++) {
    //         if (i < right) {
    //             dp[i] = Math.min(right - i, dp[2 * center - i]);
    //         }

    //         while (i - dp[i] - 1 >= 0 && i + dp[i] + 1 < s.length() && s.charAt(i - dp[i] - 1) == s.charAt(i + dp[i] + 1)) {
    //             dp[i]++;
    //         }

    //         if (i + dp[i] > right) {
    //             center = i;
    //             right = i + dp[i];
    //         }

    //         if (dp[i] > maxLen) {
    //             maxLen = dp[i];
    //             maxStr = s.substring(i - dp[i], i + dp[i] + 1).replaceAll("#", "");
    //         }
    //     }

    //     return maxStr;
    // }
}