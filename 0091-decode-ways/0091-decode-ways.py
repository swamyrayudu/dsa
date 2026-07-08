class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        next1 = 1
        next2 = 0
        for i in range(n-1,-1,-1):
            if s[i] == '0':
                next2 = next1
                next1 = 0
            else:
                one_digit = next1
                two_digit = 0
                if i + 1 < n and 10<=int(s[i:i+2])<=26:
                    two_digit = next2
                next2 = next1
                next1 = one_digit+two_digit
        return next1