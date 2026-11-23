class TimeMap:

    def __init__(self):
        self.kvpair = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvpair:
            self.kvpair[key] = []
        self.kvpair[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.kvpair.get(key, [])
        l, r = 0, len(vals)-1
        res = ""
        while l<=r:
            m = (l+r)//2
            if vals[m][1] <= timestamp:
                res = vals[m][0]
                l = m+1
            else:
                r = m-1
        return res
