class Solution:
    def minPartitions(self, n: str) -> int:
        mx = 0
        for char in n:
            mx = max(ord(char) - ord('0'), mx)
        
        return mx        