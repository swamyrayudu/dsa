class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {}
        for char in text:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char]+=1
        
        b = dic.get('b',0)
        a = dic.get('a',0)
        l = dic.get('l',0) // 2
        o = dic.get('o',0) // 2
        n = dic.get('n',0)
        return min(b,a,l,o,n)
        