class Solution:
    def canChange(self, start: str, target: str) -> bool:
        l1 = [[ch, ind] for ind, ch in enumerate(start) if ch != '_']
        l2 = [[ch, ind] for ind, ch in enumerate(target) if ch != '_']

        if len(l1) != len(l2):
            return False
        
        for a1, a2 in zip(l1, l2):
            c1, ind1 = a1
            c2, ind2 = a2

            if c1 != c2:
                return False
            
            if c1 == 'L' and ind1 < ind2:
                return False
            
            if c1 == 'R' and ind1 > ind2:
                return False

        return True 
        