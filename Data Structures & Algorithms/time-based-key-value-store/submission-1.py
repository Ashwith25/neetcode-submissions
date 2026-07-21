class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = self.map.get(key, []) + [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, [])

        low = 0
        hi = len(values) - 1
        res = ""
        while low <= hi:
            mid = low + (hi - low) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                low = mid + 1
            else:
                hi = mid - 1
        return res
