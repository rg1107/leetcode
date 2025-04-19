class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []
        def helper(left, right, n, currString):
            if left > n or right > n:
                return

            if left == n and right == n:
                res.append(currString)
                return
            
            if right > left:
                return
            
            if left < n:
                helper(left + 1, right, n, currString + '(')
            if right < n:
                helper(left, right + 1, n, currString + ')')

        helper(0,0,n,"")
        return res

        