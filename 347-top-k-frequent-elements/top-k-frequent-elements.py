class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        freqList = [[] for _ in range(n)]

        for ele, freq in count.items():
            freqList[freq - 1].append(ele)
        
        res = []
        elements_left = k

        for ind in range(n-1, -1, -1):
            if elements_left >= len(freqList[ind]):
                res.extend(freqList[ind])
                elements_left -= len(freqList[ind])
            elif elements_left > 0:
                res.extend(freqList[ind][:elements_left])
            else:
                break
        
        return res
                
            



