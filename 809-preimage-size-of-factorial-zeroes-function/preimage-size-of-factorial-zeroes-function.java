class Solution {
    /**
    https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/solutions/1873543/java-faster-than-100-best-explaination
     */
    public int preimageSizeFZF(int k) {
        long low = 0;
        long high = (long)Math.pow(10,10);
        
        while(low<=high){
            long mid  = low + (high-low)/2;
            long val = mid;
            long ans = 0;
            while(val!=0){
                val/=5;
                ans+=val;
            }
            if(ans==k){
                return 5;
            }else if(ans>k){
                high = mid-1;
            }else{
                low = mid+1;
            }
        }
        
        return 0;
    }
}