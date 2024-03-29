class Solution {
    public int minLengthAfterRemovals(List<Integer> nums) {
        if(nums.size()==1){
            return 1;
        }
        List<Integer> nums1=new ArrayList<>();
        List<Integer> nums2=new ArrayList<>();
		//Breaking into two arrays 
        if(nums.size()%2==1){
            for(int i=0;i<=nums.size()/2;i++){
                nums1.add(nums.get(i));
            }
            for(int i=nums.size()/2+1;i<nums.size();i++){
                nums2.add(nums.get(i));
            }
        }
        else{
            for(int i=0;i<nums.size()/2;i++){
                nums1.add(nums.get(i));
            }
            for(int i=nums.size()/2;i<nums.size();i++){
                nums2.add(nums.get(i));
            }
        }
		//Two pointer
        int i=nums1.size()-1;
        int j=nums2.size()-1;
        while(i>=0 && j>=0){
            if(nums1.get(i)<nums2.get(j)){
                nums1.remove(i);
                nums2.remove(j);
                i=nums1.size()-1;
                j=nums2.size()-1;
            }
            else{
                i=i-1;
            }
        }
        return (nums1.size()+nums2.size());
        
    }
}