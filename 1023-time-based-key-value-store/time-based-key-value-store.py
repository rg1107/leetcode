class TimeMap:

    def __init__(self):
        self.mp = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        
        idx = self._bin_search(timestamp, self.mp[key])
        if idx == -1:
            return ""
        return self.mp[key][idx][1]
    

    def _bin_search(self, timestamp: int, values) -> int:
        idx = -1
        low = 0
        high = len(values) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if values[mid][0] <= timestamp:
                idx = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return idx
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)