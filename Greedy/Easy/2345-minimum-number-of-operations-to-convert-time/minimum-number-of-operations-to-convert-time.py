class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_h, current_m = map(int, current.split(':'))
        correct_h, correct_m = map(int, correct.split(':'))
        
        current = current_h * 60 + current_m
        correct = correct_h * 60 + correct_m
        
        diff: int = correct - current
        res: int = 0
        
        for t in [60, 15, 5, 1]:
            if diff >= t:
                res += diff // t
                diff %= t
        
        return res