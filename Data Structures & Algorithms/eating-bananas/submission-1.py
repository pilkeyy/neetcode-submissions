class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        k = r
        while l <= r:
            m = (l + r) // 2 ## k
            time = 0
            for bananas in piles:
                time += math.ceil(float(bananas)/m)
            if time <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k  

        