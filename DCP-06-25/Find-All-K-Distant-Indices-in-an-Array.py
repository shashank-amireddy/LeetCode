class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        result = set()
        for j, val in enumerate(nums):
            if val == key:
                start = max(0, j - k)
                end = min(len(nums) - 1, j + k)
                for i in range(start, end + 1):
                    result.add(i)
        return sorted(result)

        