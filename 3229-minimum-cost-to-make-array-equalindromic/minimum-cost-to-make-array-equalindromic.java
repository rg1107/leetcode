class Solution {
    public boolean isPal(int n) {
        long r, sum = 0, temp;
        temp = n;
        while (n > 0) {
            r = n % 10;
            sum = (sum * 10) + r;
            n = n / 10;
        }
        return temp == sum;
    }

    public long calculateCost(int[] nums, int r) {
        long cost = 0;
        for (int n : nums) {
            cost += Math.abs(n - r);
        }
        return cost;
    }

    public long minimumCost(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int middle = 0;
        if (n == 1) return 0;

        if (n % 2 != 0) {
            middle = nums[n / 2];
        } else {
            middle = (nums[(n + 1) / 2] + nums[n / 2]) / 2;
        }
        long ans = (long)1e15;
        if (isPal(middle)) {
            ans = calculateCost(nums, middle);
        }

        long low = middle - 1;
        long high = middle + 1;
        long left = -1, right = -1;
        while (left == -1 || right == -1) {
            if (left == -1 && isPal((int) low)) {
                left = low;
            }
            if (right == -1 && isPal((int) high)) {
                right = high;
            }
            low--;
            high++;
        }

        return Math.min(ans, Math.min(calculateCost(nums, (int) right), calculateCost(nums, (int) left)));
    }
}