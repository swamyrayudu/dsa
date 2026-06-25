class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        dic = {}
        tdic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        for char in target:
            if char not in tdic:
                tdic[char] = 1
            else:
                tdic[char] += 1
        ans = float('inf')
        for char in target:
            ans = min(ans,dic.get(char,0)//tdic[char])
        return ans