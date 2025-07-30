class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sm = float('inf')
        mi = float('inf')
        for i in nums:
            if i > mi:
                return True
            if i <= sm:
                sm = i
            else:
                mi = i
        return False
        