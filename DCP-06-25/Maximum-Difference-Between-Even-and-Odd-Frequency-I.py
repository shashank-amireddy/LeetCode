from collections import Counter
from math import inf

class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        maxOdd = 0
        minEven = inf

        for freq in cnt.values():
            if freq % 2 == 1: 
                maxOdd = max(maxOdd, freq)
            else: 
                minEven = min(minEven, freq)

        return maxOdd - minEven

        