class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = [0] * (len(citations) + 1)

        for i in range(len(citations)):
            n[min(citations[i], len(citations))] += 1
        print(n)
        curr = 0
        for i in range(len(n) - 1, -1, - 1):
            curr += n[i]
            if curr >= i:
                return i
