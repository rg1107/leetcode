class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        vert, hori = defaultdict(lambda: [float('inf'), 0]), defaultdict(lambda: [float('inf'), 0])
        x_min, x_max, y_min, y_max = float('inf'), 0, float('inf'), 0

        for x, y in coords:
            vert[x][:] = min(vert[x][0], y), max(vert[x][1], y)
            hori[y][:] = min(hori[y][0], x), max(hori[y][1], x)
            x_min, x_max, y_min, y_max = min(x_min, x), max(x_max, x), min(y_min, y), max(y_max, y)

        ans = 0

        for x, (y_min_on_x, y_max_on_x) in vert.items():
            ans = max(ans, (y_max_on_x-y_min_on_x) * max(x-x_min, x_max-x))

        for y, (x_min_on_y, x_max_on_y) in hori.items():
            ans = max(ans, (x_max_on_y-x_min_on_y) * max(y-y_min, y_max-y))

        return ans or -1