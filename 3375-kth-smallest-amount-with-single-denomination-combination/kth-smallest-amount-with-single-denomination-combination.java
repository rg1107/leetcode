class Solution {
    /**
        https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/solutions/5020004/inclusion-and-exlusion-binarysearch-beats-100-java
        https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/solutions/5019504/python3-math-inclusion-exclusion-principle-binary-search
     */
    public long findKthSmallest(int[] coins, int k) {
        long min = coins[0];
        long max=coins[0];
        for(int i=0;i<coins.length;i++){
            min=Math.min(coins[i],min);
            max=Math.max(coins[i],max);
        }
        long left=1;
        long right=1000000000000000000L;
        long ans=Long.MAX_VALUE;
        while(left<right){
            long mid=left+(right-left)/2;
            if(isGreaterk(mid,coins,k)){
                ans=Math.min(mid,ans);
                right=mid;
            }else{
                left=mid+1;
            }
        }
        return ans;
    }
    public boolean isGreaterk(long mid, int []coins,long k){
        long l = countUniqueMultiples(coins,mid);
        // System.out.println(mid+" "+l);
        if(l>=k){
            return true;
        }
        return false;
    }
      public  long countUniqueMultiples(int[] numbers, long k) {
        return countMultiplesRecursive(numbers, k, 1, 0, -1);
    }

    private long countMultiplesRecursive(int[] numbers, long k, long lcm, int depth, int lastIdx) {
         long count = 0;
         if(depth==numbers.length){
             return 0;
         } 
        // Inclusion-exclusion principle: include or exclude sets of numbers
        for (int i = lastIdx + 1; i < numbers.length; i++) {
            long newLcm = depth == 0 ? numbers[i] : lcm(lcm,numbers[i]);

            // Calculate the count of multiples for the current LCM
            long currentMultipleCount = (k) / newLcm;

            // Include if depth is even, exclude if odd (inclusion-exclusion principle)
            if (depth % 2 == 0) {
                count += currentMultipleCount;
            } else {
                count -= currentMultipleCount;
            }

            // Recursively process the next level, increasing the depth
            count += countMultiplesRecursive(numbers, k, newLcm, depth + 1, i);
        }

        return count;
    }

    // Helper method to calculate the least common multiple
        public static long lcm(long a, long b) {
        return a / gcd(a, b) * b;  // Rearrange to avoid overflow
    }

    // Helper method to calculate the greatest common divisor
    public static long gcd(long a, long b) {
        while (b != 0) {
            long t = b;
            b = a % b;
            a = t;
        }
        return a;
    }
}