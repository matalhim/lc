class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        summ, cur = 0, 0
        st = 0
        for i in range(len(gas)):
            summ += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                st = i + 1
                cur = 0
        return st if summ >= 0 else -1