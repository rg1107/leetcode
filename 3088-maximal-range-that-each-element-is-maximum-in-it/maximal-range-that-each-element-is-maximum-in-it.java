class Solution {
    public int[] maximumLengthOfRanges(int[] nums) {
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];
        Stack<Integer> idxStack = new Stack<>();

        // Calculate left boundaries
        for (int currIdx = 0; currIdx < n; currIdx++) {
            while (!idxStack.empty() && nums[idxStack.peek()] < nums[currIdx]) {
                idxStack.pop();
            }
            left[currIdx] = idxStack.empty() ? -1 : idxStack.peek();
            idxStack.push(currIdx);
        }

        // Clear the stack for reuse
        idxStack.clear();

        // Calculate right boundaries
        for (int currIdx = n - 1; currIdx >= 0; currIdx--) {
            while (!idxStack.empty() && nums[idxStack.peek()] < nums[currIdx]) {
                idxStack.pop();
            }
            right[currIdx] = idxStack.empty() ? n : idxStack.peek();
            idxStack.push(currIdx);
        }

        // Calculate the maximal range for each element
        int[] ans = new int[n];
        for (int currIdx = 0; currIdx < n; currIdx++) {
            ans[currIdx] = right[currIdx] - left[currIdx] - 1;
        }

        return ans;
    }

    // Short Ans (1 Pass)
    /** 
    public int[] maximumLengthOfRanges(int[] nums) {
        int[] ans = new int[nums.length];
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        for (int i = 0; i <= nums.length; i++) {
            while (stack.peek() != -1 && 
                (i == nums.length || nums[stack.peek()] < nums[i])) {
                ans[stack.pop()] = i - 1 - stack.peek();
            }
            stack.push(i);
        }
        return ans;
    }
    */
}