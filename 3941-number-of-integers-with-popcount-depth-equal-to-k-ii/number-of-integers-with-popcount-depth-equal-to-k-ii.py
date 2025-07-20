class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [[0] * 6 for _ in range(self.n * 4)]
        self.build(0, self.n - 1, 1, nums)
    
    def build(self, left, right, node, nums):
        if left == right:
            depth = self.get_depth(nums[left])
            self.tree[node][depth] = 1
            return
        
        mid = left + (right - left) // 2
        self.build(left, mid, node*2, nums)
        self.build(mid + 1, right, node * 2 + 1, nums)

        for i in range(6):
            self.tree[node][i] = self.tree[node*2][i] + self.tree[node*2 +1][i]
    
    def update(self, index, val, left, right, node):
        if left == right:
            self.tree[node] = [0] * 6
            new_depth = self.get_depth(val)
            self.tree[node][new_depth] = 1
            return
        
        mid = left + (right - left) // 2

        if index <= mid:
            self.update(index, val, left, mid, node * 2)
        else:
            self.update(index, val, mid + 1, right, node * 2 + 1)
        
        for i in range(6):
            self.tree[node][i] = self.tree[node * 2][i] + self.tree[node * 2 + 1][i]
    
    def get_depth(self, i):
        d = 0
        while i > 1:
            i = bin(i).count('1')
            d += 1
        return d
    
    def get_number(self, left, right, tleft, tright, node, k):
        if right < tleft or left > tright:
            return 0
        
        if left <= tleft and tright <= right:
            return self.tree[node][k]
        
        mid = tleft + (tright - tleft) // 2
        return self.get_number(left, right, tleft, mid, node * 2, k) + self.get_number(left, right, mid + 1, tright, node * 2 + 1, k)


class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        tree = SegmentTree(nums)
        res = []
        for q in queries:
            if q[0] == 1:
                _, l, r, k = q
                res.append(tree.get_number(l, r, 0, tree.n - 1, 1, k))
            else:
                _, idx, val = q
                tree.update(idx, val, 0, tree.n - 1, 1)
        return res


# class Solution:
#     def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         def getBits(num):
#             setbit = 0
#             while (num > 0):
#                 setbit += (num & 1)
#                 num >>= 1

#             return setbit
        
#         @cache
#         def popDepth(num):
#             if num == 1:
#                 return 0
#             if num == 2:
#                 return 1
#             if num == 3:
#                 return 2

#             return 1 + popDepth(getBits(num))

#         dp = dict()
#         dpi = [0] * len(nums)
#         result = []

#         for index, num in enumerate(nums):
#             depth = popDepth(num)

#             if depth not in dp:
#                 dp[depth] = set()
                
#             dp[depth].add(index)
#             dpi[index] = depth

#         for query in queries:
#             if (query[0] == 1):
#                 l = query[1]
#                 r = query[2]
#                 k = query[3]

#                 indexes = dp.get(k, None)

#                 if indexes is None:
#                     result.append(0)
#                     continue

#                 count = 0
#                 for index in indexes:
#                     if index >= l and index <= r:
#                         count += 1

#                 result.append(count)
#             else:
#                 index = query[1]
#                 val = query[2]
                
#                 dep = dpi[index]
#                 dp.get(dep).remove(index)
#                 nums[index] = val

#                 dep = popDepth(val)

#                 if dep not in dp:
#                     dp[dep] = set()
                    
#                 dp.get(dep).add(index)
#                 dpi[index] = dep

#         return result
                
                
        