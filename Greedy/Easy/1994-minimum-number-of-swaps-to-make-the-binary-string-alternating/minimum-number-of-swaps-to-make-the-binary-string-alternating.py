class Solution:
    def minSwaps(self, s: str) -> int:
        def count_miss(st_char):
            c = 0
            for char in s:
                if char != st_char:
                    c += 1
                st_char = '0' if st_char == '1' else '1'
            return c

        o_count = s.count('1')
        z_count = len(s) - o_count
        if abs(o_count - z_count) > 1:
            return -1
        
        if o_count > z_count:
            return count_miss('1') // 2
        elif o_count < z_count:
            return count_miss('0') // 2
        else:
            return min(count_miss('0'), count_miss('1')) // 2
    
        



        