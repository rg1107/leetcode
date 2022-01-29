class Solution {
    public int minFlips(String target) {
        
        char bit = '0';
        int count = 0;
        
        for(int i=0;i<target.length();i++) {
            if(target.charAt(i)==bit) {
                continue;
            } else {
                count++;
                bit = invert(bit);
            }
        }
        
        return count;
    }
    
    private char invert(char c) {
        return c=='0'?'1':'0';
    }
}