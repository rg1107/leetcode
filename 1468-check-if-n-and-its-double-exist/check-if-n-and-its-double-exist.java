class Solution {
    public boolean checkIfExist(int[] arr) {
        Set<Integer> set = new HashSet<>();

        for (int i=0;i<arr.length;i++) {
            if (set.contains(arr[i]*2)) {
                return true;
            } else {
                set.add(arr[i]);
            }
        }

        set.clear();

        for (int i=arr.length-1;i>=0;i--) {
            if (set.contains(arr[i]*2)) {
                return true;
            } else {
                set.add(arr[i]);
            }
        }

        return false;
    }
}