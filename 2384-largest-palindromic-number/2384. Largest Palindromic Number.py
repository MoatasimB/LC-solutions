class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        counts = defaultdict(int)

        for d in num:
            counts[d] += 1
        
        p = ""
        mid = float("-inf")

        for i in "9876543210":
            if i in counts:
                pairs = counts[i] // 2
                p += i * pairs

                counts[i] -= pairs * 2
            
            if i in counts and counts[i] >= 1:
                if mid == float("-inf"):
                    mid = i
                else:
                    continue
        

        s_p = []

        i = 0
        while i < len(p) and p[i] == "0":
            i += 1
        
        while i < len(p):
            s_p.append(p[i])
            i+= 1
        
        final = []
        if mid != float("-inf"):
            final = s_p + [mid] + s_p[::-1]
        else:
            final = s_p + s_p[::-1]
        
        return ("".join(final) if final else "0")