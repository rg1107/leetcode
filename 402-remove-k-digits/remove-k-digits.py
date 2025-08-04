class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #Got the intuition right but could not think of stack solution.
        numStack = []
        
        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
        
            numStack.append(digit)
        
        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        finalStack = numStack[:-k] if k else numStack
        
        # trip the leading zeros
        return "".join(finalStack).lstrip('0') or "0"


        
        
        
        # start = 0
        # n = len(num)
        # end = 1

        # if k >= n:
        #     return "0"

        # while end < n:
        #     if ord(num[start]) >= ord(num[end]):
        #         start = end
            
        #     k -= 1
        #     end += 1
        #     if k == 0:
        #         break
        
        
        # res = ""

        # if num[start] != '0':
        #     res += num[start] 
        #     res += num[end:]
        # else:
        #     while end < n and num[end] == '0':
        #         end += 1
        #     res += num[end:]
        
        # if res == "":
        #     res = "0"
        
        # return res
        