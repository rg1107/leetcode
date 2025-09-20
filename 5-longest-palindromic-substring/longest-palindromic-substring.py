class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        temp = "#" + "#".join(s) + "#"
        n = len(temp)
        z = [0 for _ in range(n)]
        left = 0
        right = 0

        for index in range(1, n):
            if index < right:
                z[index] = min(right-index, z[left + (right - index)]) # Left Mirror or distance from right bound
            else:
                z[index] = 0
            
            # Expand current window
            while (index - z[index] - 1) >=0  and (index + z[index] + 1) < n and temp[index - z[index] - 1] == temp[index + z[index] + 1]:
                z[index] += 1

            # Update Bounds
            if index + z[index] > right:
                right = index + z[index]
                left = index - z[index]
        
        res = 1
        start = 0
        for index in range(n):
            l = z[index]
            if l > res:
                res = l
                start = (index - l)//2
        
        return s[start: start+res]





        

        