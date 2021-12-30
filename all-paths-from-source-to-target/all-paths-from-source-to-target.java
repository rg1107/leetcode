class Solution {
    
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        if(graph.length==0){
            return res;
        }
        
        List<Integer> temp = new ArrayList<>();
        temp.add(0);
        helper(graph,temp, 0);
        return res;
    }
    
    public void helper(int[][] graph, List<Integer> temp, int curr) {
        if(curr==graph.length-1) {
            if(temp.get(0)==0) {
                List<Integer> temp1 = new ArrayList<>(temp);
                res.add(temp1);
            }
        }
        
        for(int i = 0;i<graph[curr].length;i++){
                temp.add(graph[curr][i]);
                helper(graph, temp, graph[curr][i]);
                temp.remove(temp.size()-1);   
        }
        
        
    }
}