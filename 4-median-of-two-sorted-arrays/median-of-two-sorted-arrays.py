class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        left = 0
        right = m
        l = (m + n + 1) // 2

        while left <= right:
            part1 = (left + right)//2
            part2 = l - part1

            l1 = float("-inf") if part1 == 0 else nums1[part1 - 1]
            l2 = float("-inf") if part2 == 0 else nums2[part2 - 1]
            r1 = float("inf") if part1 == m else nums1[part1]
            r2 = float("inf") if part2 == n else nums2[part2]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2))/2
            elif l1 > r2:
                right = part1 - 1
            else:
                left = part1 + 1
        
        return -1

            
        