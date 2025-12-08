class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        words = set(words)
        bold = [False] * len(s)

        for word in words:
            l = 0
            r = len(word) - 1

            while r < len(s):
                if s[l : r + 1] in words:
                    for i in range(l, r + 1):
                        bold[i] = True
                l += 1
                r += 1
        

        ans = []

        i = 0
        while i < len(s):
            if bold[i]:

                ans.append("<b>")
                while i < len(s) and bold[i]:
                    ans.append(s[i])
                    i += 1
                ans.append("</b>")
            else:
                ans.append(s[i])
                i += 1
        
        return "".join(ans)

