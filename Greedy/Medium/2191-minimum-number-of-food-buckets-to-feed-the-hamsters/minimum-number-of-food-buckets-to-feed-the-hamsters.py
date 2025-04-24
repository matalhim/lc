class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        h = list(hamsters)
        res = 0
        i = 0
        while i < len(h):
            if h[i] == 'H':
                if i + 2 < len(h) and h[i + 1] == '.' and h[i + 2] == 'H':
                    h[i + 1] = '-'
                    res += 1
                    i += 3 
                elif i + 1 < len(h) and h[i + 1] == '.':
                    h[i + 1] = '-'
                    res += 1
                    i += 1
                elif i - 1 >= 0 and h[i - 1] == '.':
                    h[i - 1] = '-'
                    res += 1
                    i += 1
                else:
                    return -1
            else:
                i += 1
        return res