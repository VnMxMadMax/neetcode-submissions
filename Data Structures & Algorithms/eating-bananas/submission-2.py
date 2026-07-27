import math

# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         maxPile = max(piles)

#         speed = 1
#         while speed <= maxPile:
#             hours = 0

#             for pile in piles:
#                 hours += math.ceil(pile / speed)

#             if hours <= h:
#                 return speed

#             speed += 1

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        maxPile = max(piles)

        mid = 1

        while left <= right:

            mid = left + (right-left)//2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left
            
            
