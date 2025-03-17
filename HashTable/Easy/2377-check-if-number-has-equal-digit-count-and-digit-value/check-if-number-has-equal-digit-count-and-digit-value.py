class Solution:
    def digitCount(self, num: str) -> bool:
        freq: dict = {}
        for s in num:
            if s in freq:
                freq[s] += 1
            else:
                freq[s] = 1
        
        for i in range(len(num)):
            if int(num[i]) != freq.get(str(i), 0):
                return False
        
        return True