class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:

        counts = defaultdict(int)

        for b in bulbs:
            counts[b] += 1


        return sorted([b for b, v in counts.items() if v % 2])