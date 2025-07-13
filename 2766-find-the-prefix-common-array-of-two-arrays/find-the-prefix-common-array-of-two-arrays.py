class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        mapA = set()
        mapB = set()

        n = len(A)

        res = [0] * n
        
        for index in range(n):
            if A[index] == B[index]:
                res[index] += 1
            else:
                if A[index] in mapB:
                    res[index] += 1
                if B[index] in mapA:
                    res[index] += 1
            
            if index > 0:
                res[index] += res[index - 1]

            mapA.add(A[index])
            mapB.add(B[index])
        
        return res

        