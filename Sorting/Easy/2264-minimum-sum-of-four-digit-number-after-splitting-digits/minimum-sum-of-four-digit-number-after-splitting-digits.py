class Solution:
    def minimumSum(self, num: int) -> int:
        n_list: list = []
        while num > 0:
            n_list.append(num % 10)
            num = num // 10
        return sum(sorted(n_list)[:2]) * 10 + sum(sorted(n_list)[2:])
        