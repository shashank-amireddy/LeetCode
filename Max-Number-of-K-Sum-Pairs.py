class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count  = 0
        counts = {}
        for num in nums:
            c = k - num
            if c in counts and counts[c]>0:
                count +=1
                counts[c] -= 1
            else:
                counts[num] = counts.get(num,0)+1
        return count        