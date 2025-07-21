# Cache all prime numbers
N = 5 * (10 ** 4) + 1
seive = [True] * (N)
seive[0] = seive[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if not seive[i]: continue
    for j in range(i*i, N, i):
        seive[j] = False


class Solution:
    # https://leetcode.com/problems/count-prime-gap-balanced-subarrays/solutions/6872738/easy-sliding-window-min-max-monotonic-queue-python-o-n
    def primeSubarray(self, nums: List[int], k: int) -> int:
        maxval = deque([])
        minval = deque([])
        plist = deque([])

        l, cnt = 0, 0

        for r, x in enumerate(nums):
            if seive[x]:
                plist.append(r)
            
                while maxval and x > nums[maxval[-1]]:
                    maxval.pop()
                
                maxval.append(r)

                while minval and x < nums[minval[-1]]:
                    minval.pop()
                
                minval.append(r)

                while len(plist) >= 2 and maxval and minval and nums[maxval[0]] - nums[minval[0]] > k:
                    if seive[nums[l]]:
                        plist.popleft()
                        if maxval[0] == l:
                            maxval.popleft()
                        if minval[0] == l:
                            minval.popleft()
                    l += 1
        
            if len(plist) >= 2 and nums[maxval[0]] - nums[minval[0]] <= k:
                index = plist[-2]
                cnt += (index - l + 1)
    
        return cnt



        