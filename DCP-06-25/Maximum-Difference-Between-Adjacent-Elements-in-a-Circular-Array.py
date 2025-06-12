class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        n = len(nums)
        
        for i in range(n):
            next_i = (i + 1) % n
            diff = abs(nums[i] - nums[next_i])
            max_diff = max(max_diff, diff)
        
        return max_diff
