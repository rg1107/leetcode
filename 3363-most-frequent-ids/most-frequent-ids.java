class Solution {
    /**
        https://leetcode.com/problems/most-frequent-ids/solutions/4916730/c-java-explained-using-heap-and-without-using-heap-very-simple
     */
    public long[] mostFrequentIDs(int[] nums, int[] freq) {
        long[] ans = new long[nums.length];
        HashMap<Integer, Long> idToFreqMap = new HashMap<>();
        PriorityQueue<Pair<Long, Integer>> maxHeap = new PriorityQueue<>((a, b) -> Long.compare(b.getKey(), a.getKey()));
        for(int i = 0; i < nums.length; ++i){
            idToFreqMap.put(nums[i], idToFreqMap.getOrDefault(nums[i], 0L) + freq[i]);
            maxHeap.add(new Pair<>(idToFreqMap.get(nums[i]), nums[i]));
            while(idToFreqMap.get(maxHeap.peek().getValue()) != maxHeap.peek().getKey()) maxHeap.poll();
            ans[i] = maxHeap.peek().getKey();
        }
        return ans;
    }
}