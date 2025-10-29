class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.bookings:
            if startTime < end and endTime > start:
                newStart = max(startTime, start)
                newEnd = min(endTime, end)

                if self.check(newStart, newEnd):
                    return False
        
        self.bookings.append([startTime, endTime])
        return True
    
    def check(self, newStart, newEnd):
        overlapCount = 0
        for start, end in self.bookings:
            if newStart < end and newEnd > start:
                overlapCount += 1
                if overlapCount >= 2:
                    return True
        return False


        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)