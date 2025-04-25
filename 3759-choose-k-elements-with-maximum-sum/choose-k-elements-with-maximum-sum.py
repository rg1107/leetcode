class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        res = [0] * len(nums1)
        lasttotal = 0
        last = -1

        minHeap = [[num, i] for i, num in enumerate(nums1)]
        heapq.heapify(minHeap)

        heap2 = []
        curtotal = 0
        while minHeap:
            val, idx = heapq.heappop(minHeap)
            
            if val == last:
                res[idx] = lasttotal
                heapq.heappush(heap2, nums2[idx])
                curtotal += nums2[idx]
                last = val
            else:
                last = val
                while heap2 and len(heap2) > k:
                    v = heapq.heappop(heap2)
                    curtotal -= v

                res[idx] = curtotal
                lasttotal = curtotal
                curtotal += nums2[idx]
                heapq.heappush(heap2, nums2[idx])
                
        return res
    
    # def findMaxSum(self, nums1: List[int], 
    #                      nums2: List[int], k: int) -> List[int]:

    #     n, sm, prev  = len(nums1), 0, 0
    #     heap, ans = [], [0] * n

    #     idx = sorted(range(n), key = lambda x: nums1[x])

    #     for i in idx:
    #         num1, num2 = nums1[i], nums2[i]
            
    #         if prev < num1: prv_sum = sm
    #         ans[i] = prv_sum
                
    #         prev = num1
    #         sm+= num2

    #         if len(heap) == k:
    #             sm-= heappushpop(heap, num2)
    #         else:
    #             heappush(heap, num2)    
            
    #     return ans
        