class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        
        free: int = 0
        i: int = len(cost) - 3
        while i >= 0:
            free += cost[i]
            i -= 3
        
        return sum(cost) - free

        
        