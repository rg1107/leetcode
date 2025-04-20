class Solution:
    def resultArray(self, A: List[int], k: int) -> List[int]:
        res = [0] * k
        cnt = [0] * k
        for a in A:
            cnt2 = [0] * k
            for i, c in enumerate(cnt):
                cnt2[i * a % k] += c
                res[i * a % k] += c
            cnt = cnt2
            cnt[a % k] += 1
            res[a % k] += 1
        return res
        
        
        