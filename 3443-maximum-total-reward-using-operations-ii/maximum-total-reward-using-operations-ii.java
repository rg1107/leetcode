class Solution {

    Map<Integer, Integer> dp = new HashMap<>();
    
    public int maxTotalReward(int[] arr) {        
        arr = removeDups(arr);
        return arr[arr.length-1] + rec(arr, arr[arr.length-1] - 1);
    }
    
    private int rec(int[] arr, int lim) {
        if (lim == 0) {
            return 0;
        }
        if (dp.get(lim) != null) {
            return dp.get(lim);
        }
        int ind = find(arr, lim);
        if (ind == -1) {
            return lim;
        }
        int res = 0;
        for (int i = 0; i < ind; i++) {
            res = Math.max(res, arr[i] + rec(arr, Math.min(lim - arr[i], arr[i] - 1)));
        }
        dp.put(lim, res);
        return res;
    }
    
    private int find(int[] arr, int x) {
        int lo = 0;
        int hi = arr.length - 1;
        int res = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == x) {
                return -1;
            } else if (arr[mid] < x) {
                lo = mid + 1;
            } else {
                res = mid;
                hi = mid - 1;
            }
        }
        return res;
    }
    
    private int[] removeDups(int[] arr) {
        Set<Integer> set = new HashSet<>();
        for (int num: arr) {
            set.add(num);
        }
        int[] res = new int[set.size()];
        int i =0;
        for (int num: set) {
            res[i++] = num;
        }
        Arrays.sort(res);
        return res;
    }



    // public int maxTotalReward(int[] rewardValues) {
    //     // In case of duplicate values, we can select only one of them at any time, so removing duplicates while calculating.
    //     Set<Integer> set = new HashSet<>();
    //     int max = 0;
    //     for (int num : rewardValues) {
    //         set.add(num);
    //         max = Math.max(num, max);
    //     }
        
    //     List<Integer> list = set.stream().collect(Collectors.toList());
    //     Collections.sort(list);
    //     int n = list.size();
    //     int[][] dp = new int[n][2*max+1];
    //     for (int i=0;i<n;i++) {
    //         Arrays.fill(dp[i], -1);
    //     }
        
    //     helper(0, 0, list, n, dp);
    //     return dp[0][0];
    // }
    
    // public int helper(int curr, int ind, List<Integer> rewards, int n, int[][] dp) {
    //     if (ind >= n) {
    //         return curr;
    //     }
        
    //     if (dp[ind][curr] != -1) {
    //         return dp[ind][curr];
    //     }
        
    //     // To select or not to select is the choice here.
    //     if (curr < rewards.get(ind)) {
    //         dp[ind][curr] = Math.max(helper(curr + rewards.get(ind), ind + 1, rewards, n, dp), dp[ind][curr]);
    //         //max = Math.max(helper(curr + rewards.get(ind), ind + 1, rewards, n, dp), max);
    //     }
        
    //     dp[ind][curr] = Math.max(helper(curr, ind + 1, rewards, n, dp), dp[ind][curr]);
    //     //max = Math.max(helper(curr, ind + 1, rewards, n, dp), max);
        
    //     return dp[ind][curr];
    // }
}