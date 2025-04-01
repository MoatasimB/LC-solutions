class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        pairs = []

        for i in range(1, len(weights)):
            pair = weights[i-1] + weights[i]

            pairs.append(pair)
        
        pairs.sort()

        ans = 0

        for i in range(k-1):
            smallest = pairs[i]
            largest = pairs[len(weights) - 2 - i]
            ans += largest - smallest
        
        return ans
