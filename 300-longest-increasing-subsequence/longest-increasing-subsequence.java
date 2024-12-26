class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> arr = new ArrayList<>();

        int LIS = 1;
        arr.add(nums[0]);

        for (int i =1;i<nums.length;i++) {
            if (nums[i] > arr.get(arr.size() - 1)) {
                arr.add(nums[i]);
                LIS++;
            } else {
                int index = Collections.binarySearch(arr, nums[i]);
                if (index < 0) {
                    index = -(index + 1);
                }
                arr.set(index, nums[i]);
            }
        }

        return LIS;

        
    }
}