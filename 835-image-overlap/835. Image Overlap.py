class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        pos1 = set()
        pos2 = set()

        for r in range(n):
            for c in range(n):
                if img1[r][c]:
                    pos1.add((r, c))
                if img2[r][c]:
                    pos2.add((r, c))
        
        deltas = defaultdict(int)
        ans = 0
        for r1, c1 in pos1:
            for r2, c2 in pos2:
                dx, dy = r2 - r1, c2 - c1
                deltas[(dx, dy)] += 1
                
        return max(deltas.values()) if deltas.values() else 0
