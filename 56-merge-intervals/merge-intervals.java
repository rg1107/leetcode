class Solution {
    public int[][] merge(int[][] intervals) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(intervals, (a,b) -> a[0]-b[0]);
        int s = intervals[0][0];
        int e = intervals[0][1];
        boolean flag = false;

        for(int i=1;i<intervals.length;i++) {
            if(e>=intervals[i][0]) {
                s = Math.min(s, intervals[i][0]);
                e = Math.max(e, intervals[i][1]);
            }
            else {
                addInterval(res, s, e);
                s = intervals[i][0];
                e = intervals[i][1];
            }
        }

        addInterval(res, s, e);

        int[][] fin;

        if(intervals.length==1) {
            fin = new int[1][2];
            fin[0][0] = s;
            fin[0][1] = e;
        } else {
            fin = new int[res.size()][2];
            for(int i=0;i<res.size();i++) {
                fin[i][0] = res.get(i).get(0);
                fin[i][1] = res.get(i).get(1);
            }
        }

        return fin;
        
    }

    private void addInterval(List<List<Integer>> res, int s, int e) {
        List<Integer> temp = new ArrayList<>();
        temp.add(s);
        temp.add(e);
        res.add(temp);
    }
}