class Solution:
    def myPow(self, x: float, n: int) -> float:

        isNeg = n < 0

        n = abs(n)

        def recurse(x, n):
            if n == 0:
                return 1.0
            if n== 1:
                return x
            
            half = recurse(x, n//2)
            if n%2 == 0:
                return half * half
            else:
                return half * half * x
        
        res = recurse(x, n)
        if isNeg:
            return 1/res
        
        return res
        

        