class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = 1
        for pile in piles:
            end = max(end,pile)
        res = end
        while start <= end:
            k = start + (end - start) // 2
            currHours = 0
            
            for pile in piles:
                currHours += math.ceil(pile/k)
            if currHours <= h:
                res = k
                end = k - 1
            else:
                start = k + 1
        return res