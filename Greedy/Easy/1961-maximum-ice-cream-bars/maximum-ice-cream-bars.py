class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        r = max(costs)
        res: int = 0
        count = [0] * (r + 1)

        for c in costs:
            count[c] += 1
        
        for i in range(1, len(count)):
            if coins > 0:
                if count[i] > 0 :
                    i_c = min(count[i], coins // i)
                    res += i_c
                    coins -= i_c * i
            else:
                return res
        return res



        