class Solution {
    /**
    https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/solutions/3673330/java-beats-100-o-n-time-two-pointers-very-easy-solution
     */
    public int minimumOperations(int[] nums) {
        int l = 0, r = nums.length-1;
        int opr = 0;
        int leftSum = nums[l], rightSum = nums[r];
        while(l < r) {
            if(leftSum == rightSum) {
                l++;
                r--;
                leftSum = nums[l];
                rightSum = nums[r];
            } else if(leftSum < rightSum) {
                opr++;
                l++;
                leftSum += nums[l];
            } else {
                opr++;
                r--;
                rightSum += nums[r];
            }
        }

        return opr;
    }
}