class Solution(object):
    def twoSum(self, nums, target):
        value_to_index = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in value_to_index:
                return [value_to_index[complement], index]
            value_to_index[value] = index
        # If no solution is found, return an empty list (though the problem guarantees a solution)
        return []

        