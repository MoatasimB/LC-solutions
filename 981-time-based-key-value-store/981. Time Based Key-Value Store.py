class TimeMap:

    def __init__(self):
        self.dic  = defaultdict(list) #key : [time, val]

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        
        timestamps = self.dic[key]
        l = 0
        r = len(timestamps) - 1
        ans = ""
        while l <= r:
            mid = (l + r) // 2

            if timestamps[mid][0] <= timestamp:
                ans = timestamps[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)