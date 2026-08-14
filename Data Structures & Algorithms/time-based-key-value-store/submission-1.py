class TimeMap:

    def __init__(self):
        self.map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.map:
            return ""
        
        vals = self.map[key]

        l, r = 0, len(vals)-1
        res = ""

        while l <= r:
            m = l + (r-l)//2
            t, v = vals[m]

            if t <= timestamp:
                l = m+1
                res = v
            else:
                r = m-1
        
        return res

