class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        l, r = 0, n
        perm = []
        for char in s:
            if char == 'I':
                perm.append(l)
                l += 1
            else:  
                perm.append(r)
                r -= 1
        perm.append(l)
        return perm

        