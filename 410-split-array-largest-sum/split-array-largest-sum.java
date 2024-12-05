class Solution {
    /**
    https://leetcode.com/problems/split-array-largest-sum/solutions/1899033/java-simple-and-easy-solution-beats-100    
     */
    public int splitArray(int[] nums, int m) {
        int low = 0, high = 0;
        
        for (int n: nums) {
            low = Math.max(low, n);
            high += n;
        }
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (check(nums, m, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
    
    // check if it is possbile to split to m subarrays which each subarry's sum less than or equal to mid
    private boolean check(int[] nums, int m, int mid) {
        int sum = 0;
        int numOfSubarrays = 1;
        
        for (int i = 0; i < nums.length; i ++) {
            sum += nums[i];
            if (sum > mid) {
                numOfSubarrays ++;
                sum = nums[i];
            }
        }
        
        return numOfSubarrays <= m;
    }
}