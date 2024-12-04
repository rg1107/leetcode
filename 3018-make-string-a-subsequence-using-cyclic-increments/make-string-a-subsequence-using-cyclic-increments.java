class Solution {
    public boolean canMakeSubsequence(String str1, String str2) {
        int pt = 0; //Point to char in str2;
        int n = str1.length();
        int m = str2.length();

        for (int index=0;index<n;index++) {
            if (pt == m) {
                return true;
            }
            if ((str1.charAt(index) == str2.charAt(pt)) || 
                ((str1.charAt(index) - 97 + 1)% 26 == (str2.charAt(pt) - 97))) {
                    pt++;
            }
        }

        if (pt == m) {
            return true;
        }
        return false;
    }
}