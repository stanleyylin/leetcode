class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] += -trip[0]
        
        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False
        return True

        # timestamps = []
        # for numPassengers, start, end in trips:
        #     timestamps.append([start, numPassengers])
        #     timestamps.append([end, -numPassengers])
        
        # timestamps.sort()

        # used_capacity = 0
        # for time, passenger_change in timestamps:
        #     used_capacity += passenger_change
        #     if used_capacity > capacity:
        #         return False
        # return True