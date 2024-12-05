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

    // boolean canChange(string st, string tar) {
    //     int n=tar.length();
    //     int i=0,j=0;
    //     while(i<=n && j<=n){
            
    //         while(i<n && tar[i]=='_') i++;
    //         while(j<n && st[j]=='_') j++;
            
    //         if(i==n || j==n){
    //             return i==n && j==n;
    //         }
            
    //         if(tar[i]!=st[j]) return false;
            
    //         if(tar[i]=='L'){
    //             if(j<i) return false;
    //         }
    //         else{
    //             if(i<j) return false;
    //         }
            
    //         i++;
    //         j++;
    //     }
    //     return true;
    // }
}