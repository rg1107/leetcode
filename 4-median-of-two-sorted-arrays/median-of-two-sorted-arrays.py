class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            # Binary search will be on the shorter of the two arrays to make O(log(min(m,n)))
            return self.findMedianSortedArrays(nums2, nums1)
        
        mid_len = (m + n + 1)//2
        low = 0
        high = m

        while low <= high:
            mmid = low + (high - low) // 2
            nmid = mid_len - mmid
            
            l1, l2 = float("-inf"), float("-inf")
            r1, r2 = float("inf"), float("inf")

            if mmid - 1 >= 0: 
                l1 = nums1[mmid-1]

            if nmid - 1 >= 0:
                l2 = nums2[nmid - 1]
            
            if mmid >= 0 and mmid < m:
                r1 = nums1[mmid]
            
            if nmid >= 0 and nmid < n:
                r2 = nums2[nmid]
            
            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = mmid - 1
            else:
                low = mmid + 1
        
        return -1