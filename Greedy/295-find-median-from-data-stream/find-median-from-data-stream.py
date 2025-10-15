class MedianFinder:
    def __init__(self):
        self.high = [] # min heap for upper half
        self.low = [] # max heap for lower half, should be - for max
        # keep len(low) + 1 == len(high) or len(low) == len(high)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low)) # the num might acc belong in upper 
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (self.high[0] - self.low[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()