class Solution {
    /**
    https://leetcode.com/problems/two-best-non-overlapping-events/solutions/6124334/100-beats-simple-binary-search
     */
    public int maxTwoEvents(int[][] events) {
        int n = events.length;
        
        // Step 1: Sort the events by their start time
        Arrays.sort(events, (a, b) -> a[0] - b[0]);
        
        // Step 2: Create the suffix array for the maximum event value from each event onward
        int[] suffixMax = new int[n];
        suffixMax[n - 1] = events[n - 1][2];  // Initialize the last event's value
        
        // Populate the suffixMax array
        for (int i = n - 2; i >= 0; --i) {
            suffixMax[i] = Math.max(events[i][2], suffixMax[i + 1]);
        }
        
        // Step 3: For each event, find the next event that starts after it ends
        int maxSum = 0;
        
        for (int i = 0; i < n; ++i) {
            int left = i + 1, right = n - 1;
            int nextEventIndex = -1;
            
            // Perform binary search to find the next non-overlapping event
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (events[mid][0] > events[i][1]) {
                    nextEventIndex = mid;
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            
            // If a valid next event is found, update the max sum
            if (nextEventIndex != -1) {
                maxSum = Math.max(maxSum, events[i][2] + suffixMax[nextEventIndex]);
            }
            
            // Also consider the case where we take only the current event
            maxSum = Math.max(maxSum, events[i][2]);
        }
        
        return maxSum; 
    }

    // public int helper (int[][] dp, int k, int n, int[][] events, int i, int j) {
    //     if (i >= n || j <= k) {
    //         return 0;
    //     }
        
    //     if (dp[i][j] != -1) {
    //         return dp[i][j];
    //     }
    //     int index = findNextNonOverlappingEvent(i, events, n);
    //     dp[i][j] = Math.max(helper(dp, k, n, events, i+1, j), events[i][2] + helper(dp, k, n, events, index, j+1));
    //     return dp[i][j];
    // }

    // private int findNextNonOverlappingEvent(int i, int[][] events, int n) {
    //     for (int j = i + 1; j < n;j++) {
    //         if (events[j][0] >= events[i][1]) {
    //             return j;
    //         }
    //     }
    //     return n;
    // }
}