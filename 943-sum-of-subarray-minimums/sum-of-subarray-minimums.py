class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        nextLeft = [idx for idx in range(n)]
        nextRight = [idx for idx in range(n)]

        stack = []

        for idx in range(n):
            if not stack or arr[idx] > arr[stack[-1]]:
                nextLeft[idx] = idx - 1
            else:
                while stack and arr[idx] <= arr[stack[-1]]:
                    stack.pop()
                
                if not stack:
                    nextLeft[idx] = -1
                else:
                    nextLeft[idx] = stack[-1]
            stack.append(idx)

        stack = []

        for idx in range(n-1, -1, -1):
            if not stack or arr[idx] > arr[stack[-1]]:
                nextRight[idx] = idx + 1
            else:
                while stack and arr[idx] < arr[stack[-1]]:
                    stack.pop()
                
                if not stack:
                    nextRight[idx] = n
                else:
                    nextRight[idx] = stack[-1]
            stack.append(idx)
        
        MOD = 10 ** 9 + 7
        count = 0

        # print(nextLeft)
        # print(nextRight)

        for idx in range(n):
            m = max(0, idx - nextLeft[idx] - 1)
            n = max(0, nextRight[idx] - idx - 1)

            # print(m, n)

            count = (count + (m*n + m + n + 1)*arr[idx]) % MOD
        
        return count

        