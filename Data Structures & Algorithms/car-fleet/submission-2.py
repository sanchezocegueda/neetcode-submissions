class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position
        # new data structure, sort by position
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort(key=lambda x:x[0])

        num_fleets = 1

        p, v = cars[-1]
        fleet_time = (target - p) / v

        for i in range(n-1, -1, -1):
            car_i = cars[i]
            
            p_i, v_i = car_i

            t_i = (target - p_i) / v_i

            if t_i > fleet_time:
                fleet_time = t_i
                num_fleets += 1



        return num_fleets
