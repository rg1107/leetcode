class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        stack = []

        stack.append(nums[0])
        n = len(nums)

        for idx in range(1, n):
            gd = gcd(nums[idx], stack[-1])
            if gd > 1:
                top = stack.pop()
                lcm = (top * nums[idx])//gd
                
                while stack and gcd(lcm, stack[-1]) > 1:
                    top = stack.pop()
                    lcm = (top * lcm) // gcd(lcm, top)
                
                stack.append(lcm)
            else:
                stack.append(nums[idx])
        
        return stack
    
    def gcd(self, a, b):
        if a > b:
            return gcd(b, a)
        
        if a % b == 0:
            return b
        
        if a == 1:
            return a
        
        return gcd(b % a, a)