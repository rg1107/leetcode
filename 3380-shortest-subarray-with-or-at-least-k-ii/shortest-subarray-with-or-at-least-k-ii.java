/**
    https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/solutions/4948082/c-java-python-2-approaches-sliding-window-binary-search-two-pointers
 */
class Solution {
    private void update(int[] bits, int x, int change) {
        // insert or remove element from window, time: O(32)
        for (int i = 0; i < 32; i++) {
            if (((x >> i) & 1) != 0) {
                bits[i] += change;
            }
        }
    }

    private int bitsToNum(int[] bits) {
        // convert 32-size bits array to integer, time: O(32)
        int result = 0;
        for (int i = 0; i < 32; i++) {
            if (bits[i] != 0) {
                result |= 1 << i;
            }
        }
        return result;
    }

    private boolean isSpecial(int[] nums, int k, int len) {
        // checks if special subarray exists for length len, time: O(n)
        int n = nums.length;
        int[] bits = new int[32];
        for (int i = 0; i < n; i++) {
            update(bits, nums[i], 1); // insert nums[i] into window
            if (i >= len) {
                update(bits, nums[i - len], -1); // remove nums[i - len] from window
            }
            if (i >= len - 1 && bitsToNum(bits) >= k) {
                // special subarray found
                return true;
            }
        }
        return false;
    }

    // public int minimumSubarrayLength(int[] nums, int k) {
    //     int n = nums.length, start = 1, end = n + 1, mid;
    //     while (start < end) {
    //         mid = (start + end) / 2;
    //         if (!isSpecial(nums, k, mid)) {
    //             start = mid + 1;
    //         } else {
    //             end = mid;
    //         }
    //     }
    //     return start != n + 1 ? start : -1;
    // }

    public int minimumSubarrayLength(int[] nums, int k) {
        int n = nums.length, result = n + 1;
        int[] bits = new int[32];
        for (int start = 0, end = 0; end < n; end++) {
            update(bits, nums[end], 1); // insert nums[end] into window
            while (start <= end && bitsToNum(bits) >= k) {
                result = Math.min(result, end - start + 1);
                update(bits, nums[start++], -1); // remove nums[start] from window
            }
        }
        return result != n + 1 ? result : -1;
    }
}