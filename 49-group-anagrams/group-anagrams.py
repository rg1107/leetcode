class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = dict()

        for string in strs:
            sorted_string = ''.join(sorted([c for c in string]))
            if sorted_string not in mp:
                mp[sorted_string] = []
            mp[sorted_string].append(string)
        
        return [mp[sorted_string] for sorted_string in mp]