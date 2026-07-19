class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        mpp = {ch: i for i, ch in enumerate(s)}
        unique = len(mpp)
        n = len(s)

        ans = []
        have = set()

        for i, ch in enumerate(s):
            if ch in have:
                continue
            
            while ans and (ans[-1] > ch and mpp[ans[-1]] > i):
                have.remove(ans[-1])
                ans.pop()

            ans.append(ch)
            have.add(ch)
        
        return "".join(ans)