class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        res = letters[0]
        while l <= r:
            m = l + (r - l) // 2
            if ord(letters[m]) > ord(target):
                r = m - 1
                res = letters[m]
            else:
                l = m + 1

        return res
        