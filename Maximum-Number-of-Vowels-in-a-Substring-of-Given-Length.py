class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        curr =  sum(c in vowels for c in s[:k])
        max_count = curr

        for i in range(k, len(s)):
            curr += (s[i] in vowels) - (s[i-k] in vowels)
            max_count = max(max_count, curr)
        return max_count
        