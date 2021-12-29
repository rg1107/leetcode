class Solution {
    public int[] executeInstructions(int n, int[] startPos, String s) {
        
        int len = s.length();
        int[] res = new int[len];
        char[] sarr = s.toCharArray();
        int borderTop = startPos[0]+1;
        int borderBot = n-startPos[0];
        int borderLeft = startPos[1]+1;
        int borderRight = n-startPos[1];
        Map<Integer, Integer> horizontal = new HashMap();
        horizontal.put(0, len);
        Map<Integer, Integer> vertical = new HashMap();
        vertical.put(0, len);
        Map<Character, int[]> dirs = new HashMap();
        dirs.put('L', new int[]{0,1});
        dirs.put('R', new int[]{0,-1});
        dirs.put('U', new int[]{1,0});
        dirs.put('D', new int[]{-1,0});
        int[] pos = new int[2];
        for(int i=len-1; i>=0; i--){
            int[] increment = dirs.get(sarr[i]);
            pos[0]+=increment[0];
            pos[1]+=increment[1];
            int local = len-i;
            if(vertical.containsKey(pos[0]-borderTop))
                local = Math.min(local, vertical.get(pos[0]-borderTop)-i-1);
            if(vertical.containsKey(pos[0]+borderBot))
                local = Math.min(local, vertical.get(pos[0]+borderBot)-i-1);
            if(horizontal.containsKey(pos[1]-borderLeft))
                local = Math.min(local, horizontal.get(pos[1]-borderLeft)-i-1);
            if(horizontal.containsKey(pos[1]+borderRight))
                local = Math.min(local, horizontal.get(pos[1]+borderRight)-i-1);
            vertical.put(pos[0], i);
            horizontal.put(pos[1], i);
            res[i] = local;
        }
        return res;
        
    }
}