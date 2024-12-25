class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = len(t)
        needDic = defaultdict(int)
        for ch in t:
            needDic[ch] +=1

        have = 0
        l = 0
        currDic = defaultdict(int)
        length = float("inf")
        start = 0
        for r in range(len(s)):

            if s[r] in needDic:
                currDic[s[r]] +=1
                if currDic[s[r]] <= needDic[s[r]]:
                    have +=1

            while have == need:
                if length > r - l + 1:
                    length = r-l+1
                    start = l
                if s[l] in needDic:
                    currDic[s[l]] -=1
                    if currDic[s[l]] < needDic[s[l]]:
                        have -=1
                l+=1
        return s[start: start + length] if length != float('inf') else ""
            




