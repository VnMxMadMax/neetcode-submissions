class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(a, b) for a, b in zip(position, speed)]
        pair.sort()

        fleet = []
        # Iterate from right to left (closest to the target first)
        for pos, spd in reversed(pair):
            # Calculate time as a float
            time = (target - pos) / spd
            
            if not fleet or time > fleet[-1]:
                fleet.append(time)
                
        return len(fleet)

