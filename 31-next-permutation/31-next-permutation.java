class Solution {
    public void nextPermutation(int[] nums) {
        
        int k = -1;
        int l = -1;
        
        for(int i = nums.length-2;i>=0;i--) {
            if(nums[i]<nums[i+1]) {
                k = i;
                break;
            }
        }
        
        if(k==-1) {
            Arrays.sort(nums);
            return;
        }
        
        for(int i = nums.length-1;i>k;i--) {
            if(nums[k]<nums[i]) {
                l = i;
                break;
            }
        }
        
        int temp = nums[k];
        nums[k] = nums[l];
        nums[l] = temp;
        
        int st = k+1;
        int en = nums.length-1;
        
        while(st<en) {
            temp = nums[st];
            nums[st] = nums[en];
            nums[en] = temp;
            
            st++;
            en--;
        }
    }
}