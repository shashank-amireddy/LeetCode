class Solution:
    def compress(self, chars: List[str]) -> int:
        i =0
        ctr = 1
        for j in range(1,len(chars)+1):
            if j < len(chars) and chars[j] == chars[j-1]:
                ctr += 1
            else:
                chars[i] = chars[j-1]
                i+=1
                if ctr > 1:
                    for k in str(ctr):
                        chars[i] = k
                        i+=1
                ctr = 1
        return i