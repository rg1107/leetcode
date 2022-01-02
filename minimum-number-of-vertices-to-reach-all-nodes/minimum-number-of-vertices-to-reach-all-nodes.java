class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        
        List<List<Integer>> res = new ArrayList<>();
        int[] indeg = new int[n];
        for(int i=0;i<n;i++) {
            res.add(new ArrayList<>());
            indeg[i] = 0;
        }
        
        
        for(List<Integer> edge : edges) {
            res.get(edge.get(0)).add(edge.get(1));
            indeg[edge.get(1)]++;
        }
        
        int[][] sort = new int[n][2];
        
        for(int i=0;i<n;i++) {
            sort[i][0] = i;
            sort[i][1] = indeg[i];
        }
        
        Arrays.sort(sort, (a,b)->a[1]-b[1]);
        
        int[] vis = new int[n];
        Arrays.fill(vis, 0);
        
        List<Integer> set = new ArrayList<>();
        
        for(int i=0;i<n;i++){
            if(vis[sort[i][0]]!=2) {
                DFS(sort[i][0], res, vis);
                set.add(sort[i][0]);
            }
        }
        
        return set;
        
    }
    
    private void DFS(int u, List<List<Integer>> res, int[] vis) {
        vis[u] = 1;
        
        for(int i =0;i<res.get(u).size();i++) {
            if(vis[res.get(u).get(i)]!=2) {
                DFS(res.get(u).get(i), res, vis);
            }
        }
        
        vis[u] = 2;
    }
    
}