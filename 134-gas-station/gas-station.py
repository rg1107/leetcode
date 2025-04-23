class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        spareGas: int = 0
        start: int = -1
        currGas: int = 0
        first: bool = True

        for index, (g, c) in enumerate(zip(gas, cost)):
            spareGas += (g-c)
            currGas += (g-c)

            if currGas >= 0 and first:
                start = index
                first = False

            if currGas < 0:
                currGas = 0
                start = -1
                first = True
        
        if spareGas < 0:
            return -1
        
        return start
            
            

        