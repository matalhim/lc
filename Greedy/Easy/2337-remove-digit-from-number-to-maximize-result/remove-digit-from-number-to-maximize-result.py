class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        j: int = 0

        for i, char in enumerate(number):
            if char == digit:
                j = i
                if i + 1 < len(number) and int(char) < int(number[i + 1]):
                    return number[:i] + number[i+1:]
        
        return number[:j] + number[j+1:]

                
                    