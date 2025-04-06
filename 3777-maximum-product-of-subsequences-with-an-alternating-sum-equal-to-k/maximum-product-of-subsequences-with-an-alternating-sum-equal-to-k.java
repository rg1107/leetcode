class Solution {
    public int maxProduct(int[] nums, int k, int limit) {
        // int[][][] dp = new int[nums.length][2][k+1
        HashMap<List<Integer>, Integer> dp = new HashMap<>();
        int sum=0;
        for(int i:nums) sum += i;
        sum = Math.min(900, sum);
        if(k<-sum || k>sum) return -1;
        return helper(nums, 0, 0, limit, 1, k, dp);
    }

    public int helper(int[] nums, int i, int turn, int limit, int product, int k, HashMap<List<Integer>, Integer> dp){
        if(i==nums.length && k==0 && product<=limit && turn!=0) return product;
        
        if(i==nums.length) return -1;
        if(product>limit) product=limit+1;
        // int[] temp = new int[]{i, turn, product, k};
        // String temp = i+""+turn+""+product+""+k;
        List<Integer> temp = new ArrayList<>();
        temp.add(i);
        temp.add(turn);
        temp.add(product);
        temp.add(k);
        if(dp.containsKey(temp)) {
            // System.out.println("hello");
            return dp.get(temp);
        }
        int ans=-1;
        ans = Math.max(ans, helper(nums, i+1, turn, limit , product, k,dp));
        ans = Math.max(ans, helper(nums, i+1,(turn==2?1:2), limit, product*nums[i], k-(turn==2?-nums[i]:nums[i]),dp));
        dp.put(temp, ans);
        return ans;
        
    }
}