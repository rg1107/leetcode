class Solution {
    public int beautifulSplits(int[] nums) {
        int res = 0;
        int[] zall = z(nums);
        for (int i = 1; i <= nums.length - 2; i++) {
            int[] zpart = z(nums, i);
            // not a pref of 2nd split
            for (int j = i + 1; j < i * 2; j++) {
                if (nums.length - j < j - i) {
                    break;
                }
                if (zpart[j - i] >= j - i) {
                    res++;
                }
            }
            // can be a pref of 2nd split
            if (zall[i] >= i) {
                res += nums.length - 2 * i; // all splits are beautiful
            } else {
                for (int j = i * 2; j <= nums.length - 1; j++) {
                    if (nums.length - j < j - i) {
                        break;
                    }
                    if (zpart[j - i] >= j - i) {
                        res++;
                    }
                }
            }
        }
        return res;
    }

    static int[] z(int[] s) {
        int n = s.length;
        int[] z = new int[n];
        int l = 0, r = 0;
    
        for (int i = 1; i < n; i++) {
            if (i <= r) {
                z[i] = Math.min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
                z[i]++;
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        return z;
    }

    static int[] z(int[] s, int i) {
        int n = s.length - i;
        int[] z = new int[n];
        int l = 0, r = 0;
    
        for (int k = 1; k < n; k++) {
            if (k <= r) {
                z[k] = Math.min(r - k + 1, z[k - l]);
            }
            while (k + z[k] < n && s[i + z[k]] == s[i + k + z[k]]) {
                z[k]++;
            }
            if (k + z[k] - 1 > r) {
                l = k;
                r = k + z[k] - 1;
            }
        }
        return z;
    }
}