class Solution {
    public List<Integer> pathInZigZagTree(int label) {
        return path(label,0);  
    }
    public List<Integer> path(int label, int level) {
        while (1 << level <= label) ++level;
        List<Integer> l=new ArrayList<>();
        for(; label >= 1; label /= 2, --level) {
            l.add(label);
            label = (1 << level) - 1 - label + (1 << (level - 1));
        }
        Collections.reverse(l);
        return l;
    }  
}