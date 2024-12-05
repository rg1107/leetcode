class Solution {
    public boolean canChange(String start, String target) {
        if (start.length() != target.length()) {
            return false;
        }
        List<Integer> sIndex = new ArrayList<>();
        List<Integer> tIndex = new ArrayList<>();

        for (int i=0;i<start.length();i++) {
            if (start.charAt(i) != '_') {
                sIndex.add(i);
            }
        }

        for (int i=0;i<target.length();i++) {
            if (target.charAt(i) != '_') {
                tIndex.add(i);
            }
        }

        if (sIndex.size() != tIndex.size()) {
            return false;
        }

        for (int i=0;i<sIndex.size();i++) {
            char s = start.charAt(sIndex.get(i));
            char t = target.charAt(tIndex.get(i));
            if (s != t) {
                return false;
            }
            if (s == 'L' && sIndex.get(i) < tIndex.get(i)) {
                return false;
            }
            if (s == 'R' && sIndex.get(i) > tIndex.get(i)) {
                return false;
            }
        }

        return true;
    }

    // Map<Integer, Integer> posMap = new HashMap<>();
    //     int i = 0;
    //     int j = 0;
    //     int m = start.length();
    //     int n = target.length();
    //     while (i < m && j < n) {
    //         while (j< n && target.charAt(j) == '_') {
    //             j++;
    //         }
    //         while (i < m && j<n && start.charAt(i) != target.charAt(j)) {
    //             i++;
    //         }
    //         if (i < m && j<n) {
    //             posMap.put(i, j);
    //             j++;
    //         }
    //     }

    //     if (j < n) {
    //         return false;
    //     }

    //     for (Map.Entry<Integer, Integer> entry: posMap.entrySet()) {
    //         int sIndex = entry.getKey();
    //         int tIndex = entry.getValue();

    //         if (start.charAt(sIndex) == 'L' && sIndex < tIndex) {
    //             return false;
    //         }

    //         if (start.charAt(sIndex) == 'R' && sIndex > tIndex) {
    //             return false;
    //         }
    //     }

    //     return true;
}