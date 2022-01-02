class Solution {
    public int minAddToMakeValid(String s) {
        int c = 0;
        
        Stack<Character> st = new Stack<>();
    
        
        for(int i=0;i<s.length();i++) {
            if(st.isEmpty() && s.charAt(i)==')') {
                c++;
            }
            else if(s.charAt(i)=='(') {
                st.push(s.charAt(i));
            }
            else if(s.charAt(i)==')' && !st.isEmpty()) {
                st.pop();
            }
            
        }
        
        return c + st.size();
        
    }
}