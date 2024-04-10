/**
    Intuition
    When navigating the graph, we use bitwise AND operations between edges to calculate the path's cost.
    Additionally, we can reuse the same edges multiple times.
    By performing bitwise AND, the cost may decrease or remain the same.
    Hence, our objective is to maximize edge utilization to minimize path cost.
    We can organize vertices into groups reachable via connected edges.
    Within each group, traversing any two nodes results in the same cost since we traverse all edges in the group,
    ensuring the minimum cost. Consequently, for each group of interconnected vertices, the cost remains constant, equivalent to the AND operation of all connecting edges within the group.

    Approach
    Perform union find on edges to find the groups of connected vertices
    During the union-find operation, maintain a list called weights to represent the weight of each connected group. When performing a union operation between two vertices, compute the new weight of the group by performing a bitwise AND operation between the existing weight of each group and the cost of the edge connecting them. This process updates the cost of the group of vertices to reflect the addition of the new edge
    All weights are initialized to 131071. 131071 is chosen because it is 11111111111111111 in binary and is greater than 10^5.
    When returning result for a query if si is equal to ti return 0 because start and target are same
    If si and ti don't belong to the same group return -1
    If si and ti are members of the same group, return the result of performing the AND operation on all edges within that group.
 */

class DSU {
    int[] parent, rank, weights;
    public DSU(int n) {
        parent = new int[n];
        rank = new int[n];
        weights = new int[n];
        Arrays.fill(weights, 131071);
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }
    public int find(int x) {
        if (x != parent[x])
            parent[x] = find(parent[x]);
        return parent[x];
    }
    public void union(int x, int y, int weight) {
        int xx = find(x);
        int yy = find(y);
        if (rank[xx] < rank[yy])
            parent[xx] = yy;
        else
            parent[yy] = xx;
        weights[xx] = weights[yy] = weights[xx] & weights[yy] & weight;
        if (rank[xx] == rank[yy])
            rank[xx]++;
    }
    public int minimumCostOfWalk(int x, int y) {
        if (x == y)
            return 0;
        if (find(x) != find(y))
            return -1;
        return weights[find(x)];
    }
}

class Solution {
    public int[] minimumCost(int n, int[][] edges, int[][] query) {
        DSU uf = new DSU(n);
        for (int[] edge : edges)
            uf.union(edge[0], edge[1], edge[2]);
        int[] result = new int[query.length];
        for (int i = 0; i < query.length; i++)
            result[i] = uf.minimumCostOfWalk(query[i][0], query[i][1]);
        return result;
    }
}