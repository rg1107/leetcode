class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        isPrime = [True for _ in range(n)]

        isPrime[0] = False
        isPrime[1] = False

        for p in range(2, ceil(sqrt(n))):
            if isPrime[p]:
                for idx in range(p*p, n, p):
                    isPrime[idx] = False

        count = sum(isPrime)
        return count        