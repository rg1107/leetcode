class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mp = dict()

        for r in replacements:
            if r[0] not in mp:
                mp[r[0]] = [r[1], False] # Value with resolved Flag

        def helper(text, mp):
            arr = text.split('%')
            res = arr[0]
            n = len(arr)

            for index in range(1, n):
                if index % 2 == 0:
                    res += arr[index]
                    continue
                else:
                    temp, isResolved = mp[arr[index]]
                    if isResolved:
                        res += temp
                    else:
                        temp = helper(temp, mp)
                        mp[arr[index]] = [temp, True]
                        res += temp
            
            return res

        return helper(text, mp)

        