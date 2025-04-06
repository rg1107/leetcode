class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        N = len(nums)
        L = [i for i in range(-1, N)]
        R = [i for i in range(1, N+1)]

        self.inversions = sum(nums[i] > nums[i+1] for i in range(N-1))
        S = SortedList([nums[i] + nums[i+1], i] for i in range(N-1))

        def add(i):
            j = R[i]
            if 0 <= i < j < N:
                S.add([nums[i] + nums[j], i])
                self.inversions += nums[i] > nums[j]
        
        def remove(i):
            j = R[i]
            if 0 <= i < j < N:
                S.discard([nums[i] + nums[j], i])
                self.inversions -= nums[i] > nums[j]
        
        ans = 0

        while self.inversions:
            ans += 1
            s, i = S.pop(0)
            j = R[i]
            h, k = L[i], R[j]

            remove(h)
            remove(i)
            remove(j)

            nums[i] += nums[j]
            R[i] = k
            if k < N:
                L[k] = i
            
            add(h)
            add(i)
        
        return ans
        