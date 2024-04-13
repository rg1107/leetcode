class Solution {
    public int[] minimumTime(int n, int[][] edges, int[] disappear) {
        Map<Integer, List<int[]>> map = new HashMap<>();
        for (int[] i : edges) {
            int x = i[0];
            int y = i[1];
            int len = i[2];
            map.putIfAbsent(x, new ArrayList<>());
            map.putIfAbsent(y, new ArrayList<>());
            map.get(x).add(new int[]{y, len});
            map.get(y).add(new int[]{x, len});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(za -> za[1]));
        pq.offer(new int[]{0, 0});

        int[] ans = new int[n];
        Arrays.fill(ans, -1);

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int node = curr[0];
            int time = curr[1];

            if (ans[node] != -1) {
                continue;
            }

            ans[node] = time;

            for (int[] j : map.getOrDefault(node, new ArrayList<>())) {
                int nextNode = j[0];
                int nextTime = time + j[1];
                if (nextTime < disappear[nextNode] && (ans[nextNode] == -1 || nextTime < ans[nextNode])) {
                    pq.offer(new int[]{nextNode, nextTime});
                }
            }
        }
        return ans;
    }
}