class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        dp = [[float('inf')]* (d + 1) for _ in range(n + 1)]
        
        mx = 0
        for idx in range(n-1, -1, -1):
            mx = max(mx, jobDifficulty[idx])
            dp[idx][1] = mx
        
        for job in range(n-1, -1, -1):
            for day in range(2, d+1):
                dp[job][day], max_of_day = float('inf'), 0
                for job_index in range(job, n - day + 1):
                    max_of_day = max(max_of_day, jobDifficulty[job_index])
                    dp[job][day] = min(dp[job][day], max_of_day + dp[job_index + 1][day - 1])
        
        return dp[0][d]

        
        # @functools.lru_cache(None)
        # def dfs(curr_job, days_left):
        #     if days_left == 1:
        #         return max(jobDifficulty[curr_job:])
            
        #     res, max_of_day = float('inf'), 0

        #     for job_index in range(curr_job, n - days_left + 1):
        #         max_of_day = max(max_of_day, jobDifficulty[job_index])
        #         res = min(res, max_of_day + dfs(job_index + 1, days_left - 1))
            
        #     return res
        
        # return dfs(0, d)