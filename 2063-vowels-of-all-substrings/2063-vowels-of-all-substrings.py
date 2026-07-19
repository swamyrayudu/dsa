class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        ans = 0
        for i,ch in enumerate(word):
            if ch in 'aeiou':
                ans += (i+1) * (n-i)
        return ans
