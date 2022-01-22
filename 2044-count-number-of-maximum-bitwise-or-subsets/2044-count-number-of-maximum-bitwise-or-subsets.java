class Solution {
    private int dfs(int index, int[] nums, int n, int or, int max)
    {
        if (index == n)
        {
            return (or == max) ? 1 : 0; 
        }
        return dfs(index+1, nums, n, or, max) + dfs(index+1, nums, n, or | nums[index], max); 
    }
    public int countMaxOrSubsets(int[] nums) {
        int max = 0; 
        for (int x : nums) max |= x; 
        return dfs(0, nums, nums.length, 0, max); 
        
        
    }
}