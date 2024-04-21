class Solution {
    /**
    https://leetcode.com/problems/find-edges-in-shortest-paths/solutions/5052498/dijkstra-s-algorithm-in-two-directions
    https://leetcode.com/problems/find-edges-in-shortest-paths/solutions/5052485/java-dijstra-s-algorithm-set
    */
    public boolean[] findAnswer(int n, int[][] edges) {
        ArrayList<ArrayList<int[]>> e = new ArrayList<>();
        int m = edges.length;
        for(int i = 0; i < n; i++) e.add(new ArrayList<>());
        for(int[] x : edges) {
            e.get(x[0]).add(new int[]{x[1], x[2]});
            e.get(x[1]).add(new int[]{x[0], x[2]});
        }
        long[] d1 = new long[n];
        boolean[] seen = new boolean[n];
        Arrays.fill(d1, Long.MAX_VALUE);
        d1[0] = 0;
        PriorityQueue<long[]> pq = new PriorityQueue<>(new Comparator<>() {
            public int compare(long[] a, long[] b) {
                return a[1]>b[1]?1:-1;
            }
        });
        pq.add(new long[]{0, 0});
        while(!pq.isEmpty()) {
            int curr = (int)pq.remove()[0];
            if(seen[curr]) continue;
            seen[curr] = true;
            for(int[] x : e.get(curr)) {
                if(d1[curr]+x[1] < d1[x[0]]) {
                    d1[x[0]] = d1[curr]+x[1];
                    pq.add(new long[]{x[0], d1[x[0]]});
                }
            }
        }
        
        long[] d2 = new long[n];
        seen = new boolean[n];
        Arrays.fill(d2, Long.MAX_VALUE);
        d2[n-1] = 0;
        pq = new PriorityQueue<>(new Comparator<>() {
            public int compare(long[] a, long[] b) {
                return a[1]>b[1]?1:-1;
            }
        });
        pq.add(new long[]{n-1, 0});
        while(!pq.isEmpty()) {
            int curr = (int)pq.remove()[0];
            if(seen[curr]) continue;
            seen[curr] = true;
            for(int[] x : e.get(curr)) {
                if(d2[curr]+x[1] < d2[x[0]]) {
                    d2[x[0]] = d2[curr]+x[1];
                    pq.add(new long[]{x[0], d2[x[0]]});
                }
            }
        }
        
        long min = d1[n-1];
        boolean[] ans = new boolean[m];
        for(int i = 0; i < m; i++) {
            int a = edges[i][0];
            int b = edges[i][1];
            int w = edges[i][2];
            if((long)w+d1[a]+d2[b]==min || (long)w+d1[b]+d2[a]==min) ans[i] = true;
        }
        
        return ans;
    }
}