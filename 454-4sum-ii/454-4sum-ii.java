class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        
        Map<Integer, Integer> map1 = new HashMap<>();
        Map<Integer, Integer> map2 = new HashMap<>();
        int count;
        int res = 0;
        int a, b;
        
        for(int i=0;i<nums1.length;i++) {
            for(int j=0;j<nums2.length;j++) {
                count = map1.containsKey(nums1[i] + nums2[j]) ? map1.get(nums1[i] + nums2[j]) : 0;
                map1.put(nums1[i] + nums2[j], count + 1);
            }
        }
        
        for(int i=0;i<nums3.length;i++) {
            for(int j=0;j<nums4.length;j++) {
                count = map2.containsKey(nums3[i] + nums4[j]) ? map2.get(nums3[i] + nums4[j]) : 0;
                map2.put(nums3[i] + nums4[j], count + 1);
            }
        }
        
        for(int i: map1.keySet()) {
            a = map1.getOrDefault(i, 0);
            b = map2.getOrDefault(-i,0);
            
            res += a*b;
        }
        
        return res;
        
    }
}