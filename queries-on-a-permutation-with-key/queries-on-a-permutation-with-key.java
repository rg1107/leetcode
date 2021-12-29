class Solution {
    public int[] processQueries(int[] queries, int m) {
        int p[] = new int[m];
         ArrayList<Integer> arr = new ArrayList<Integer>(queries.length);
        for(int i=0;i<m;i++){
            p[i]=i+1;
        }
        for(int i : queries){
            for(int j=0;j<m;j++){
                if(i==p[j]){
                    arr.add(j);
                    for(int k=j;j>=1;j--){
                        p[j]=p[j-1];
                    }
                    p[0]=i;
                }
            }
        }
        int [] ar = new int[arr.size()];
        for(int i=0;i<arr.size();i++){
            ar[i]=arr.get(i);
        }
        return ar;
    }
}