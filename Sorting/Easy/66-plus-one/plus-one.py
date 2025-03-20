class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int(reduce(lambda x,y: x+str(y), digits, ''))
        s += 1
        return [int(i) for i in str(s)]
        