class Solution:
    def longestPalindrome(self, s: str) -> str:
        sg = '|' + '|'.join(s) + '|'
        n = len(sg)
        P = [0] * n
        c = r = 0
        
        for i in range(1, n - 1):
            if i < r:
                m = 2 * c - i
                P[i] = min(r - i, P[m])
            
            a, b = i + (1 + P[i]), i - (1 + P[i])
            while a < n and b >= 0 and sg[a] == sg[b]:
                P[i] += 1
                a += 1
                b -= 1
            
            if i + P[i] > r:
                c, r = i, i + P[i]
        
        l, i = max((val, idx) for idx, val in enumerate(P))
        st = (i - l) // 2
        return s[st: st + l]