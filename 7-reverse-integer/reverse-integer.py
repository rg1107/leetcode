class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0
        while (x > 0):
            if (INT_MAX // 10 < res or (INT_MAX - x % 10) < res * 10):
                return 0
            res = res * 10 + x % 10
            x = x//10
        
        return sign * res;
        

        