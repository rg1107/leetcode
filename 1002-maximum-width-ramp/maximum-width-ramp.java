class Solution {
    /**
    https://leetcode.com/problems/maximum-width-ramp/solutions/208348/java-c-python-o-n-using-stack
     */
    public int maxWidthRamp(int[] A) {
        Stack<Integer> s = new Stack<>();
        int res = 0, n = A.length;
        for (int i = 0; i < n; ++i)
            if (s.empty() || A[s.peek()] > A[i])
                s.add(i);
        for (int i = n - 1; i > res; --i)
            while (!s.empty() && A[s.peek()] <= A[i])
                res = Math.max(res, i - s.pop());
        return res;
    }

    // public int maxWidthRamp(int[] A) {
    //     List<Integer> s = new ArrayList<>();
    //     int res = 0, n = A.length;
    //     for (int i = 0; i < n; ++i) {
    //         if (s.size() == 0 || A[i] < A[s.get(s.size() - 1)]) {
    //             s.add(i);
    //         } else {
    //             int left = 0, right = s.size() - 1, mid = 0;
    //             while (left < right) {
    //                 mid = (left + right) / 2;
    //                 if (A[s.get(mid)] > A[i]) {
    //                     left = mid + 1;
    //                 } else {
    //                     right = mid;
    //                 }
    //             }
    //             res = Math.max(res, i - s.get(left));
    //         }
    //     }
    //     return res;
    // }
}