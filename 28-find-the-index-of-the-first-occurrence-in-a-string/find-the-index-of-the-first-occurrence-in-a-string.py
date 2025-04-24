class Solution:
    # https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/665448/ac-simply-readable-python-kmp-rabin-karp
    def strStr(self, haystack, needle): 
        def cal(c):
            return ord(c) - ord('A')
        N = len(needle)
        H = len(haystack)
        mul =  ord('z') - ord('A') + 1
        over = sys.maxsize
        if N > H:
            return -1
        hash_needle = 0
        hash_haystack = 0
        idx_mul = mul ** (N - 1)
        for i in range(N):
            hash_needle = (mul * hash_needle + cal(needle[i])) % over
            hash_haystack = (mul * hash_haystack + cal(haystack[i])) % over
        if hash_needle == hash_haystack:
            return 0
        for i in range(1, H - N + 1):
            hash_haystack = (mul *  (hash_haystack - cal(haystack[i - 1]) * idx_mul)  + cal(haystack[i + N - 1])) % over
            if hash_needle == hash_haystack:
                return i
        return -1

    #KMP
    # def strStr(self, haystack, needle):
    #     n, h = len(needle), len(haystack)
    #     i, j, nxt = 1, 0, [-1]+[0]*n
    #     while i < n:                                # calculate next array
    #         if j == -1 or needle[i] == needle[j]:   
    #             i += 1
    #             j += 1
    #             nxt[i] = j
    #         else:
    #             j = nxt[j]
    #     i = j = 0
    #     while i < h and j < n:
    #         if j == -1 or haystack[i] == needle[j]:
    #             i += 1
    #             j += 1
    #         else:
    #             j = nxt[j]
    #     return i-j if j == n else -1
        