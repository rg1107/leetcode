class Solution {
    /*
    https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/solutions/4220643/JavaC++Python-DP
    */
    List<Integer>[] G;
    int[] vis;
    int dfs(int i, int p, int[] A, int k, int v) {
        if (v > 13) return 0;
        if (vis[i] > v) return 0;
        vis[i]++;
        int op1 = (A[i] >> v) - k, op2 = A[i] >> v + 1;
        for (int j : G[i]) {
            if (j == p) continue;
            op1 += dfs(j, i, A, k, v);
            op2 += dfs(j, i, A, k, v + 1);
        }
        return Math.max(op1, op2);
    }

    int maximumPoints(int[][] edges, int[] A, int k) {
        int n = edges.length + 1;
        G = new List[n];
        vis = new int[n];
        for (int i = 0; i < n; i++) {
            G[i] = new ArrayList();
        }
        for (int[] e : edges) {
            G[e[0]].add(e[1]);
            G[e[1]].add(e[0]);
        }
        return dfs(0, -1, A, k, 0);
    }
}