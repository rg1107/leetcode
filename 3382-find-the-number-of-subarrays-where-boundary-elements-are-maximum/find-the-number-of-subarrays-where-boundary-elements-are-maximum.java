class Solution {
    /**
    https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/solutions/5017056/java-c-python-stack-o-n
    */
    public long numberOfSubarrays(int[] A) {
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        long res = 0;
        for (int a : A) {
            while (!stack.isEmpty() && stack.peek()[0] < a)
                stack.pop();
            if (stack.isEmpty() || stack.peek()[0] != a)
                stack.push(new int[]{a, 0});
            res += ++stack.peek()[1];
        }
        return res;
    }
}