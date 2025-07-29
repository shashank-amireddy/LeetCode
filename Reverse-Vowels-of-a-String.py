class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s_list = list(s)  
        vow_indices = []
        
        for i, char in enumerate(s_list):
            if char.lower() in vowels:
                vow_indices.append(i)
        
        i, j = 0, len(vow_indices) - 1
        while i < j:
            s_list[vow_indices[i]], s_list[vow_indices[j]] = s_list[vow_indices[j]], s_list[vow_indices[i]]
            i += 1
            j -= 1
        
        return "".join(s_list)

        