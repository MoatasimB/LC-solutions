class TimeMap:

    def __init__(self):
        self.dic = {} #(key,timestamp) : val
        self.times = defaultdict(list)#key : [sorted list of most recent timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[(key,timestamp)] = value
        self.times[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.times[key]
        l = 0
        r = len(lst) - 1
        prev = -1
        while l <= r:
            mid = (l+r) // 2
            if lst[mid] <= timestamp:
                prev = max(prev, mid)
                l = mid + 1
            else:
                r = mid - 1
        

        if prev == -1:
            return ''
        return self.dic[(key, lst[prev])]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)