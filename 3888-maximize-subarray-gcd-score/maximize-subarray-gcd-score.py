class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        #https://leetcode.com/problems/maximize-subarray-gcd-score/solutions/6820683/java-c-python-pow-of-2-time-o-n-2-space-o-1
        res = 0
        n = len(nums)

        for i in range(n):
            a = nums[i]
            count = 0
            min_pow = inf

            for j in range(i, n):
                a = gcd(a, nums[j])
                low = nums[j] & -nums[j] #Finding the least set bit or lowest power of 2
                if min_pow > low:
                    min_pow = low
                    count = 0
                if min_pow == low:
                    count += 1
                
                cur = a * (2 if count <= k else 1) * (j - i + 1) # अगर लीस्ट पॉवर ऑफ़ 2 से k ज़्यादा है तो हम उन एलिमेंट्स को डबल कर सकते है जिससे जीसीडी डबल हो जाएगा।
                res = max(res, cur)
        
        return res
        