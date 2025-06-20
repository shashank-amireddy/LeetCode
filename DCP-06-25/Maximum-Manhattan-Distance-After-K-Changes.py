class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def flip(pair: str) -> int:
            res = pos = opposite = 0
            for c in s:
                if c in pair:
                    pos += 1
                else:
                    pos -= 1
                    opposite += 1
                res = max(res, pos + 2 * min(k, opposite))
            return res
        
        return max(flip("NE"), flip("NW"), flip("SE"), flip("SW"))

        