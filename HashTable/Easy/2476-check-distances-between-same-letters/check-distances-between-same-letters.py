class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dist: dict = {}
        for i in range(len(s)):
            if s[i] in dist:
                dist[s[i]] += i-1
            else:
                dist[s[i]] = -i
        
        for char in dist:
            idx = ord(char) - ord('a')
            if dist[char] != distance[idx]:
                return False
        
        return True
