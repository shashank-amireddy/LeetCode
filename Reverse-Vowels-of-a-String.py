class Solution:
    def reverseVowels(self, l: str) -> str:
        v = ['a','e','i','o','u']
        vow = []
        s=list(l)
        for i in range(len(s)):
            if (s[i].lower() in v):
                vow.append(s[i])
                s[i]=None

        for i in range(len(s)):
            if s[i] == None:
                s[i] = vow.pop()
        return "".join(s)
        