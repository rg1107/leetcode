class Solution {
    public int earliestAcq(int[][] logs, int n) {
        Arrays.sort(logs, (a,b) -> a[0] - b[0]);
        int parent[] = new int[n];
        int rank[] = new int[n];
        int groups = n;

        for (int i=0;i<n;i++){
            parent[i] = i;
            rank[i] = 0;
        }
        int ans = -1;

        for (int[] log : logs) {
            int x = log[1];
            int y = log[2];

            int parx = findParent(x, parent);
            int pary = findParent(y, parent);

            if (parx != pary) {
                if (rank[parx] > rank[pary]) {
                    parent[pary] = parx;
                    rank[parx]++;
                } else {
                    parent[parx] = pary;
                    rank[pary]++;
                }
                groups--;
            }

            if (groups == 1) {
                ans = log[0];
                break;
            }
        }

        return ans;
    }

    public int findParent(int x, int[] parent) {
        if (parent[x] == x) {
            return x;
        }
        return findParent(parent[x], parent);
    }
}