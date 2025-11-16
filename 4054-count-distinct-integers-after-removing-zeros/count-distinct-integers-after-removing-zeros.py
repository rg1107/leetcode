class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        length = len(s)

        pow9 = [1] * (length + 1)
        result = 0

        for idx in range(1, length + 1):
            pow9[idx] = pow9[idx - 1] * 9

        for d in range(1, length):
            result += pow9[d]
        
        for idx, ch in enumerate(s):
            digit = int(ch)
            
            if digit == 0:
                return result
            
            result += (digit - 1) * pow9[length - idx - 1]
        
        return result + 1
        