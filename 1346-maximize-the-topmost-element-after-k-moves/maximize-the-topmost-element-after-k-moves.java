class Solution {
    public int maximumTop(int[] nums, int k) {
        int n = nums.length;
        if (n == 1 && k%2 == 1) {
            return -1;
        }

        int max = -1;

        if (k > n) {
            max = Arrays.stream(nums).max().getAsInt();
            return max;
        } else {
            int i = 1;
            while (i < k) {
                max = Math.max(max, nums[i-1]);
                i++;
            }
            if (k < n) {
                max = Math.max(max, nums[k]);
            }
            return max;
        }
    }
}