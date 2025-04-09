class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res: int = 0

        for c in costs:
            if coins >= c:
                coins -= c
                res +=1
            else:
                return res
        return res


        