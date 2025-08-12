class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a = fruits[0]
        b = -1
        aTotal = 1
        bTotal = 0
        aEnd = 0
        bEnd = -1
        mx = 1
        n = len(fruits)

        for idx in range(1, n):
            typ = fruits[idx]
            if typ == a:
                aTotal += 1
                aEnd = idx
                mx = max(mx, aTotal + bTotal)
                continue
            
            if b == -1 or typ == b:
                bTotal += 1
                b = typ
                bEnd = idx
                mx = max(mx, aTotal + bTotal)
                continue
            
            if aEnd < bEnd:
                aTotal = 1
                bTotal = idx - aEnd - 1
                aEnd = idx
                a = typ
            else:
                bTotal = 1
                aTotal = idx - bEnd - 1
                bEnd = idx
                b = typ
            
            mx = max(mx, aTotal + bTotal)
        
        return mx
        
        

        