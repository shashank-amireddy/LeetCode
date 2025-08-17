class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]
        s= 0
        for i in gain:
            s+=i
            arr.append(s)
            
        return max(arr)
        