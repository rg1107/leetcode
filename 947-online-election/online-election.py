class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.map = dict()
        self.n = len(persons)
        self.winner = [-1] * self.n
        self.times = times
        self._calc_leader(persons, times)
    

    def _calc_leader(self, persons, times):
        idx = 0
        curr_max = 0
        for person, time in zip(persons, times):
            if person not in self.map:
                self.map[person] = 0
            
            self.map[person] += 1

            if self.map[person] >= curr_max:
                self.winner[idx] = person
                curr_max = self.map[person]
            else:
                self.winner[idx] = self.winner[idx - 1]
            
            idx += 1
        
        print(self.winner)


    def q(self, t: int) -> int:
        left = 0
        right = self.n - 1
        res = - 1
        while left <= right:
            mid = left + (right - left) // 2
            if t >= self.times[mid]:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        
        print(t, left)
        return self.winner[left-1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)