class Solution {
    /**
        https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/solutions/3867958/java-python-3-min-of-the-longest-distance-between-same-numbers
     */
    public int minimumSeconds(List<Integer> nums) {
        Map<Integer, List<Integer>> map = new HashMap<>();

        for (int i=0;i<nums.size();i++) {
            if (!map.containsKey(nums.get(i))) {
                List<Integer> freq = new ArrayList<>();
                freq.add(i);
                map.put(nums.get(i), freq);
            } else {
                map.get(nums.get(i)).add(i);
            }
        }
        int n = nums.size();
        int ans = n;
        for (var l : map.values()) {
            l.add(n + l.get(0));
            int max = 0; 
            for (int i=1;i<l.size();i++) {
                max = Math.max(max, (l.get(i) - l.get(i-1))/2);
            }
            ans = Math.min(ans, max);
        }

        return ans;
    }
}