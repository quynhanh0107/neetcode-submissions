class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        car_fleets = []
        # sort by position from closest to target -> farthest
        sorted_cars = sorted(zip(position, speed), reverse=True)

        # time for each car to get to the target: time = (target-position)/speed
        for p, s in sorted_cars:
            curr_time = (target - p)/s

            if not car_fleets:
                car_fleets.append(curr_time)
            elif curr_time > car_fleets[-1]:
                car_fleets.append(curr_time)
        
        return len(car_fleets)

