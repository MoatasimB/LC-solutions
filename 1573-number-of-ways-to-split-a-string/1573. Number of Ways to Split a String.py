class Solution:
    def numWays(self, s: str) -> int:
        
        places = []
        count = 0
        n = len(s)
        for i in range(n):
            if s[i] == "1":
                places.append(i)
                count +=1
        
        if count % 3 != 0:
            return 0
        
        if count == 0:
            return (((n-2) * (n-1)) // 2) % (10**9 + 7)

        split = count // 3

        return (places[split] - places[split-1]) * (places[split*2] - places[split*2-1]) % (10**9 + 7)