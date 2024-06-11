class Solution {
    public int maximumLength(int[] nums, int k) {
        Map<Integer, Integer>[] maps = new HashMap[k + 1];

        for (int i=0;i<k+1;i++) {
            maps[i] = new HashMap<>();
        }

        int[] res = new int[k + 1];

        for (int num : nums) {
            for (int i = k;i>=0;i--) {
                int v = maps[i].getOrDefault(num, 0);
                v = Math.max(v + 1, (i > 0 ? res[i - 1] + 1 : 0));
                maps[i].put(num, v);
                res[i] = Math.max(res[i], v);
            }
        }

        return res[k];
    }
}