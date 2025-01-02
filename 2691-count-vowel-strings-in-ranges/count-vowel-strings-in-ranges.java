class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        int[] count = new int[words.length];
        
        for(int i=0;i<words.length;i++) {
            if(isVowel(words[i])) {
                count[i] = 1;
            } else {
                count[i] = 0;
            }
        }
        
        for(int i=1;i<count.length;i++) {
            count[i] += count[i-1];
        }
        
        int[] res = new int[queries.length];
        
        for(int i=0;i<queries.length;i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            
            if (l==0) {
                res[i] = count[r];
            } else {
                res[i] = count[r] - count[l-1];
            }
        }
        
        return res;
        
    }
    
    private boolean isVowel(String s) {
        
        if(s.charAt(0)=='a' || s.charAt(0)=='e' || s.charAt(0)=='i' || s.charAt(0)=='o' || s.charAt(0)=='u' ) {
            if(s.charAt(s.length()-1)=='a' || s.charAt(s.length()-1)=='e' || s.charAt(s.length()-1)=='i' || s.charAt(s.length()-1)=='o' || s.charAt(s.length()-1)=='u') {
                return true;
            }
        }
        
        return false;
    }
}