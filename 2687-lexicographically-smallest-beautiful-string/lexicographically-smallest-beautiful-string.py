class Solution:
    """
    https://leetcode.com/problems/lexicographically-smallest-beautiful-string/solutions/3468344/python-different-three-continuous-character
    """
    def smallestBeautifulString(self, s: str, k: int) -> str:
        A = [ord(c) - ord('a') for c in s]
        i = len(A) - 1
        while i >= 0:
            A[i] += 1
            if A[i] == k:
                i -= 1
            elif A[i] not in A[max(i - 2, 0):i]:
                for j in range(i + 1, len(A)):
                    A[j] = min({0, 1, 2} - set(A[max(0, j - 2): j]))
                return ''.join(chr(ord('a') + a) for a in A)
        return ''
        
        