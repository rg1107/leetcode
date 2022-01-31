class Solution {
    public String removeOccurrences(String s, String part) {
        Stack<Character> st = new Stack<>();
        int temp = part.length();
        
        for(int i=0;i<s.length();i++) {
            st.push(s.charAt(i));
            if(st.peek()==part.charAt(part.length()-1)) {
                temp = part.length();
                while(temp>0) {
                    if(st.isEmpty() || st.peek() != part.charAt(temp-1)) {
                         break;
                    }
                    else if(st.peek() == part.charAt(temp-1)) {
                        st.pop();
                        temp--;
                    }
                }
                
                if(temp!=0) {
                    while(temp<part.length()) {
                        st.push(part.charAt(temp));
                        temp++;
                    }
                }
            }
        }
        
        StringBuilder sb = new StringBuilder("");
        while(!st.isEmpty()) {
            sb.append(st.pop());
        }
        
        return sb.reverse().toString();
    }
}