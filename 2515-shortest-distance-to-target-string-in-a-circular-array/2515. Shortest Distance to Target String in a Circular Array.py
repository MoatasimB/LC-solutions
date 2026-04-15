class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        forward = -1
        n = len(words)
        count = 0
        for i in range(startIndex, startIndex + n + 1):
            
            if words[i % n] == target:
                forward = count
                break
            count += 1
        
        count = 0
        backward = -1
        for i in range(startIndex, startIndex - n - 1, -1):
            if words[(i + n) % n] == target:
                backward = count
                break
            
            count += 1
        
        if forward == backward == -1:
            return -1
        
        return min(forward, backward)


