class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        
        Map<Integer, List<Integer>> map = new HashMap<>();
        
        int n = groupSizes.length;
        
        for(int i=0;i<n;i++) {
            if(!map.containsKey(groupSizes[i])){
                map.put(groupSizes[i], new ArrayList<>());
            }
            
            map.get(groupSizes[i]).add(i);
        }
        
        List<List<Integer>> res = new ArrayList<>();
        
        for(Integer i: map.keySet()){
            List<Integer> temp = map.get(i);
            for(int j = 0;j<temp.size();j+=i){
                List<Integer> t = new ArrayList<>();
                for(int k = j;k<j+i;k++){
                    t.add(temp.get(k));
                }
                res.add(t);
            }
        }
        
        return res;
        
    }
}