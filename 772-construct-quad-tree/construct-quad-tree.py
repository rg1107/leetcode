"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        n = len(grid)

        def helper(grid, rl, rr, cl, cr) -> 'Node':
            if rl == rr and cl == cr:
                # Leaf Node
                node = Node(grid[rl][cl] == 1, True, None, None, None, None)
                return node
            
            if rl > rr or cl > cr:
                return None

            isDifferent = False
            temp = grid[rl][cl]
            for x in range(rl, rr+1):
                for y in range(cl, cr+1):
                    if grid[x][y] != temp:
                        isDifferent = True
                        break
                
                if isDifferent:
                    break
            
            if not isDifferent:
                return Node(grid[rl][cl] == 1, True, None, None, None, None)

            rmid = (rr + rl)//2
            cmid = (cr + cl)//2

            topRight = helper(grid, rl, rmid, cmid + 1, cr)
            topLeft = helper(grid, rl, rmid, cl, cmid)
            bottomLeft = helper(grid, rmid+1, rr, cl, cmid)
            bottomRight = helper(grid, rmid + 1, rr, cmid + 1, cr)

            node = Node(grid[rl][cl] == 1, False, topLeft, topRight, bottomLeft, bottomRight)

            return node
        
        return helper(grid, 0, n-1, 0, n-1)

        