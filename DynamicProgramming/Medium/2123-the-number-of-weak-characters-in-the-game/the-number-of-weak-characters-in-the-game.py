class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        md = 0
        res = 0
        for _, d in properties:
            if d < md:
                res += 1
            else:
                md = d
        return res