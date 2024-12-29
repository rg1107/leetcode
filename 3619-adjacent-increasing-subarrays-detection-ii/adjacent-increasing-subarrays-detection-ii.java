class Solution {
    public int maxIncreasingSubarrays(List<Integer> nums) {
        int n = nums.size();
        int[] len = new int[n];
        int start = 0;
        int end = 1;
        int l = 1;

        while (end < n) {
            if (nums.get(end) > nums.get(end - 1)) {
                end++;
                l++;
                continue;
            }
            while (start < end) {
                len[start] = l;
                l--;
                start++;
            }
            l = 1;
            end++;
        }

        while (start < n) {
            len[start] = l;
            l--;
            start++;
        }

        int result = 1;

        // for (int index = 0;index < n;index++) {
        //     System.out.print(len[index] + " ");
        // }

        for (int index = 0;index < n;index++) {
            int k = len[index];
            if (k % 2 == 0) {
                result = Math.max(result, k/2); // Break the current subarray
            }
            if (index + k < n) {
                result = Math.max(result, Math.min(k, len[index + k])); // Join with another subarray
            }
        }

        return result;
    }
}