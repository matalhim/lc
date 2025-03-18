class Solution:
    def reverseWords(self, s: str) -> str:
        res: str = ''
        l: int = 0

        while l < len(s):
            while l < len(s) and s[l] == ' ':
                l += 1
                res += ' '
            r = l
            while r < len(s) and s[r] != ' ':
                r += 1
            
            res += s[l:r][::-1]
            l = r
        
        return res




        