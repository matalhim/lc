class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res: list[str] = []
        chars: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while columnNumber > 0:
            columnNumber -= 1 
            p = columnNumber % 26 
            res.append(chars[p])
            columnNumber = columnNumber // 26 
        return ''.join(reversed(res))
        