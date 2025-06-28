class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        odds = 0
        evens = 0
        n = len(nums)

        def calculateCost(par: bool, indexes: List[int], n: int):
            start = 0
            if not par:
                start = 1

            ind = 0
            cost = 0
            
            for index in range(start, n, 2):
                cost += abs(indexes[ind] - index)
                ind += 1
            
            return cost

        for num in nums:
            if num % 2 == 0:
                evens += 1
            else:
                odds += 1

        if (evens < (n // 2)) or (odds < (n // 2)):
            return -1
        
        oIndexes = []
        eIndexes = []

        cost = sys.maxsize

        for index, num in enumerate(nums):
            if num % 2 == 0:
                eIndexes.append(index)
            else:
                oIndexes.append(index)

        if evens == odds:
            cost = min(cost, calculateCost(True, oIndexes, n))
            cost = min(cost, calculateCost(True, eIndexes, n))
        elif evens > odds:
            cost = min(cost, calculateCost(True, eIndexes, n))
        else:
            cost = min(cost, calculateCost(True, oIndexes, n))
        
        return cost