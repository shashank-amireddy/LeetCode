class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums) 
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] < nums[(i + j) % len(nums)]:
                    ans[i] = nums[(i + j) % len(nums)]
                    break 
        return ans
