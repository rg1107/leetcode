class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letter = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        
        def recurse(index, digits, curr, res):
            if index >= len(digits):
                res.append(curr)
                return
            
            for c in letter[ord(digits[index]) - ord('0') - 2]:
                recurse(index + 1, digits, curr + c, res)
        
        recurse(0, digits, "", res)
        return res
        