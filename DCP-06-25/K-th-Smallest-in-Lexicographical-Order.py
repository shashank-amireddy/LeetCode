class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_count(prefix, n):
            count = 0
            curr = prefix
            next_prefix = prefix + 1
            while curr <= n:
                count += min(n + 1, next_prefix) - curr
                curr *= 10
                next_prefix *= 10
            return count

        current = 1
        k -= 1 
        while k > 0:
            count = get_count(current, n)
            if count <= k:
                k -= count
                current += 1
            else:
                current *= 10
                k -= 1
        return current

        