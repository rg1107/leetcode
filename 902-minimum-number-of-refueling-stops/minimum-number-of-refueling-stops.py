class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        fuel , heap, count = startFuel, [], 0

        stations.append([target, 0]) # storing position with stops required to reach target from that pos

        while stations:
            if fuel >= target:
                return count
            
            while stations and stations[0][0] <= fuel:
                _, liters = stations.pop(0)
                heappush(heap, -liters) # creating a max heap
            
            if not heap: return -1 # cannot reach the target, and no fueling station in range

            fuel -= heappop(heap) # Taking the station in range with max fuel

            count += 1 # refuelled in the station, increase thhe refuelling count

        return count 



        # def rec(index, fuel, pos, target, stations):
        #     if pos >= target or fuel + pos >= target:
        #         return 0
            
        #     if fuel < 0:
        #         return len(stations) + 1

        #     if index >= len(stations):
        #         if pos >= target or fuel + pos >= target:
        #             return 0
        #         else:
        #             return len(stations) + 1
            
        #     res = len(stations) + 1

        #     if index + 1 < len(stations):
        #         next_pos, _ = stations[index + 1]
        #         pos, fuel_here = stations[index]
        #         res = min(res, 1 + rec(index + 1, fuel + fuel_here - (next_pos - pos), next_pos, target, stations))
        #         res = min(res, rec(index + 1, fuel - (next_pos - pos), next_pos, target, stations))
        #     else:
        #         res = min(res, rec(index + 1, fuel, pos, target, stations))
            
        #     return res
        
        # result = rec(0, startFuel, 0, target, stations)

        # if result > len(stations):
        #     return -1
        # else:
        #     return result

        