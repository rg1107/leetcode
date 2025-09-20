class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mp = dict()
        MOD = 10 ** 9 + 7
        for point in points:
            x, y = point
            if y not in mp:
                mp[y] = 0
            mp[y] += 1
        
        l = [mp[y] for y in mp]
        res = 0
        s = 0

        if l[0] > 1:
            s = (l[0] * (l[0] - 1))//2
        
        for idx in range(1, len(l)):
            if l[idx] <= 1:
                continue
            
            a = (l[idx] * (l[idx] - 1))//2
            b = (s * a) % MOD
            res = (res + b) % MOD
            s += a
        
        return res


        