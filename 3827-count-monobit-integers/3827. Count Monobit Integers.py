class Solution:
    def countMonobit(self, n: int) -> int:
        def getBits(x):
            bits = set()
            while x:
                bits.add(x & 1)
                x = x >> 1
            return len(bits)
        ans = 1
        for i in range(1, n + 1):
            count = getBits(i)
            if count == 1:
                ans += 1 
        return ans
            
            