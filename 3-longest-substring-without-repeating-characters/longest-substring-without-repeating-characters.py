class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        start = 0

        for idx, ch in enumerate(s):
            if ch not in seen:
                seen.add(ch)
                res = max(len(seen), res)
            else:
                while start < idx and s[start] != ch:
                    seen.remove(s[start])
                    start += 1
                start += 1
        
        return res
