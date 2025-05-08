class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
             return -1
        st = 0
        cur = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0:
                st = i + 1
                cur = 0
        return st