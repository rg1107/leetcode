class Solution {
    /**
    https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/solutions/2560101/java-c-python-meeting-room
     */
    public int minGroups(int[][] intervals) {
        int res = 0, cur = 0, n = intervals.length, A[][] = new int[n * 2][2];
        for (int i = 0; i < n; ++i) {
            A[i * 2] = new int[]{intervals[i][0], 1};
            A[i * 2 + 1] = new int[]{intervals[i][1] + 1, -1};
        }
        /**
        because o[1] is either -1 or 1. So o[0] * 3 - o[1] will maintain the order of o[0],
        but when o[0] is equal for 2 elements then it will start to
        sort by o[1]

        It's the same as Arrays.sort(A, (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
         */
        Arrays.sort(A, Comparator.comparingInt(o -> o[0] * 3 + o[1]));
        for (int[] a: A)
            res = Math.max(res, cur += a[1]);
        return res;
    }
}