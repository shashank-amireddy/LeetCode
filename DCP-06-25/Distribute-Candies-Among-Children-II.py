from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = comb(n + 2, 2)
        
        for i in range(3):
            for j in range(1 << 3):
                if bin(j).count('1') != i + 1:
                    continue
                subtract_n = n - (limit + 1) * (i + 1)
                if subtract_n >= 0:
                    total += (-1) ** (i + 1) * comb(subtract_n + 2, 2)
        
        return total
