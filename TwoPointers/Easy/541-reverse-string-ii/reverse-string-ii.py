class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s: list[str] = list(s)
        n: int = len(s)
        for l in range(0, n, 2 * k):
            r: int = min(l + k, n)
            s[l:r] = s[l:r][::-1]

        return ''.join(s)


        