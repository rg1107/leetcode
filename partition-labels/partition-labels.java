class Solution {
    public List<Integer> partitionLabels(String s) {
        Map<Character, Integer> st = new HashMap<>();
        Map<Character, Integer> ed = new HashMap<>();
        
        List<Integer> res = new ArrayList<>();
        
        for(int i=0;i<s.length();i++) {
            if(!st.containsKey(s.charAt(i))) {
                st.put(s.charAt(i), i);
            }
        }
        
        for(int i = s.length()-1;i>=0;i--) {
            if(!ed.containsKey(s.charAt(i))) {
                ed.put(s.charAt(i), i);
            }
        }
        
        int[][] l = new int[st.keySet().size()][2];
        int j = 0;
        
        for(char c: st.keySet()) {
            l[j][0] = st.get(c);
            l[j][1] = ed.get(c);
            j++;
        }
        
        Arrays.sort(l, (a,b)->b[1]-a[1]);
        
        // for(int i = 0;i<l.length;i++) {
        //     System.out.println(l[i][0] + " " + l[i][1]);
        // }
        
        int m = l[0][0];
        int n = l[0][1];
        
        for(int i = 0;i<l.length;i++) {
            if(l[i][0]>=m && l[i][0]<=n){
                m = Math.min(m, l[i][0]);
                n = Math.max(n, l[i][1]);
                continue;
            }
            
            if(l[i][1]<m) {
                res.add(n-m+1);
                m = l[i][0];
                n = l[i][1];
                continue;
            }
            
            if(l[i][0]<m) {
                m = l[i][0];
                n = Math.max(n, l[i][1]);
                continue;
            }
            
        }
        
        res.add(n-m+1);
        
        Collections.reverse(res);
        
        return res;
    }
}