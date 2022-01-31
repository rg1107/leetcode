class Solution {
    List<List<Integer>> ans ;
    public List<List<Integer>> permute(int[] nums) {
        ans = new ArrayList<>();
        int index= 0;
        List<Integer> outpt = new ArrayList<>();   
        solve(nums, index);
        return ans;
    }
    
    private void solve(int []nums, int index){
        //base case
        if(index >= nums.length){
            //creating list for output
			List<Integer> output= new ArrayList<>();
			// adding all the nums from integer array
            for(int i:nums){
                output.add(i);
            }
			//final list to return
            ans.add(output);
            return ;    
        }
        
        for(int j= index; j<nums.length; j++ ){
		// swap each letter
            swap(nums, index, j);
			//recursive call for the function
            solve(nums, index+1);
			// backtracking 
            swap(nums, index,j);
        }
    }
    
	// swap function
    private void swap(int []nums, int index, int j){
        int temp = nums[index];
        nums[index] = nums[j];
        nums[j] = temp;
    }
}