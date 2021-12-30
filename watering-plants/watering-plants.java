class Solution {
    public int wateringPlants(int[] plants, int capacity) {
        
        int st = 0;
        int cap = capacity;
        
        if(plants[0]<=cap) {
            cap -= plants[0];
            st = 1;
        }
        
        for(int i=0;i<plants.length-1;i++) {
            if(cap<plants[i+1]) {
                st += 2*i + 3;
                cap = capacity - plants[i+1];
                continue;
            }
            
            cap -= plants[i+1];
            st++;
        }
        
        return st;
    }
}