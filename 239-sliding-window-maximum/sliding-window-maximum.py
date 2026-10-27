class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        n = len(nums)
        res = []

        for idx in range(n):
            while dq and nums[idx] > nums[dq[-1]]:
                dq.pop()
            
            dq.append(idx)
            
            if dq[0] <= idx - k:
                dq.popleft()
            
            if idx >= k-1:
                res.append(nums[dq[0]])
        
        
        return res

