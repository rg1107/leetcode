class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        mp = dict()
        for points in obstacles:
            x, y = points
            if x not in mp:
                mp[x] = set()
            mp[x].add(y)
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # N, E, S, W in clockwise
        curr_dir_ind = 0 # North
        x, y = 0, 0
        res = 0

        for comm in commands:
            if comm == -1:
                curr_dir_ind = (curr_dir_ind + 1) % 4
            elif comm == -2:
                curr_dir_ind = (curr_dir_ind - 1) % 4
            else:
                for step in range(comm):
                    dx, dy = directions[curr_dir_ind]
                    nx, ny = x + dx, y + dy
                    if self.isObstaclePresent(nx, ny, mp):
                        break
                    x = nx
                    y = ny

                    res = max(res, x**2 + y**2)
        return res

        
    def isObstaclePresent(self, x, y, mp):
        if x in mp:
            if y in mp[x]:
                return True
        return False
        
        