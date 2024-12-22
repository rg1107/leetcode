class Solution {
    public int maxDistinctElements(int[] arr, int diff) {
        Arrays.sort(arr);
        Set<Integer> uniqueValues = new HashSet<>();
        int last = Integer.MIN_VALUE;
        
        for (int value : arr) {
            int newPos = Math.max(last + 1, value - diff);
            if (newPos <= value + diff) {
                uniqueValues.add(newPos);
                last = newPos;
            }
        }
        
        return uniqueValues.size();
    }
}