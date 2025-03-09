class Solution:
    def coloredCells(self, n: int) -> int:
        n -= 1
        return 1 + 2*(n * (n+1))

        # 1 5 13 25
        # 1 2 3 4
        # +4 +8 +12
        
        # 0 4 12 24


        # 4(1+3+6)