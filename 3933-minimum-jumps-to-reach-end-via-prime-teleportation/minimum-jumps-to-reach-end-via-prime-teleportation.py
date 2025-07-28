class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        M = max(nums)
        isPrime = [True] * (M + 1)
        if M >= 0:
            isPrime[0] = False
        if M >= 1:
            isPrime[1] = False
        for i in range(2, int(M**0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, M + 1, i):
                    isPrime[j] = False

        tmp = defaultdict(list)
        for i, num in enumerate(nums):
            val = num
            f = 2
            while f * f <= val:
                if val % f == 0:
                    tmp[f].append(i)
                    while val % f == 0:
                        val //= f
                f += 1
            if val > 1: 
                tmp[val].append(i)

        q = deque([(0, 0)]) 
        visitedIdx = {0}
        visitedPrime = set() 

        while q:
            idx, level = q.popleft()

            if idx == n - 1:
                return level

            if isPrime[nums[idx]]:
                p = nums[idx]
                
                if p not in visitedPrime:
                    for nei in tmp[p]:
                        if nei not in visitedIdx:
                            visitedIdx.add(nei)
                            q.append((nei, level + 1))
                    
                    visitedPrime.add(p)
                    
            if idx + 1 < n and (idx + 1) not in visitedIdx:
                visitedIdx.add(idx + 1)
                q.append((idx + 1, level + 1))

            if idx - 1 >= 0 and (idx - 1) not in visitedIdx:
                visitedIdx.add(idx - 1)
                q.append((idx - 1, level + 1))
        
        return -1 



        

            
        