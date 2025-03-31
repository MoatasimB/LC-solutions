class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_seen = {ch:i for i, ch in enumerate(s)}

        ans = []
        start = 0
        last = 0
        for i in range(len(s)):
            last = max(last, last_seen[s[i]])
            # if last == len(s) - 1:
            #     ans.append(last-start + 1)
            #     return ans

            if last == i:
                ans.append(i-start + 1)
                start = i + 1
         
        return ans