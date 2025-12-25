class DetectSquares:

    def __init__(self):
        self.points = []
        self.freq = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        ans = 0
        a, b = point
        for p, count in list(self.freq.items()):
            x, y = p

            if abs(a - x) == abs(b - y) and (a, b) != (x, y):
                
                third = self.freq[(a, y)]
                fourth = self.freq[(x, b)]
                ans += third * fourth * count
        return ans

