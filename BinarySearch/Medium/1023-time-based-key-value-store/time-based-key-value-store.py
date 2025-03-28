class TimeMap:

    def __init__(self):
        self.store: dict[str, tuple[str, int]] = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key, [])
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res: str = ''
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            val, ts_prev = values[m]
            if ts_prev <= timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1

        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)