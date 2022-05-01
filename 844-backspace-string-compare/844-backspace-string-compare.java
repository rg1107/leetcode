class Solution {
    public boolean backspaceCompare(String s, String t) {
        
        Stack<Character> st = new Stack<>();
        
        for(int i=0;i<s.length();i++) {
            if(s.charAt(i)!='#') {
                st.push(s.charAt(i));
            } else {
                if(!st.isEmpty()) {
                    st.pop();
                }
            }
        }
        
        StringBuilder sbs = new StringBuilder("");
        
        while(!st.isEmpty()) {
            sbs.append(st.pop());
        }
        
        for(int i=0;i<t.length();i++) {
            if(t.charAt(i)!='#') {
                st.push(t.charAt(i));
            } else {
                if(!st.isEmpty()) {
                    st.pop();
                }
            }
        }
        
        StringBuilder sbt = new StringBuilder("");
        
        while(!st.isEmpty()) {
            sbt.append(st.pop());
        }
        
        if(sbs.toString().equals(sbt.toString())) {
            return true;
        } else {
            return false;
        }
        
        
    }
}