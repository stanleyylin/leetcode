class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamps = []
        for numPassengers, start, end in trips:
            timestamps.append([start, numPassengers])
            timestamps.append([end, -numPassengers])
        
        timestamps.sort()

        used_capacity = 0
        for time, passenger_change in timestamps:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False
        return True