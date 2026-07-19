class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(a, b) for a, b in zip(position, speed)]
        pair.sort()

        fleet = []
        # Iterate from right to left (closest to the target first)
        for pos, spd in reversed(pair):
            # Calculate time as a float
            time = (target - pos) / spd
            
            # If the current car takes longer than the fleet ahead of it,
            # it cannot catch up and forms a new fleet.
            if not fleet or time > fleet[-1]:
                fleet.append(time)
                
        return len(fleet)

