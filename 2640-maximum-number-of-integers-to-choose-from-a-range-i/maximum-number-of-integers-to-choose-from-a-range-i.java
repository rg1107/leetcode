class Solution {
    public int maxCount(int[] banned, int n, int maxSum) {
        Arrays.sort(banned);
        int total = 0, count = 0;
        for (int i = 1; i <= n; i++) {
            if (!binarySearch(banned, i)) {
                total += i;
                if (total <= maxSum) count++;
                else break;
            }
        }
        return count;
    }

    private boolean binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return true;
            if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return false;
    }   
}