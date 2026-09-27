class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        mpp = {}
        for key, val in knowledge:
            mpp[key] = val
        

        stack = []
        final = []
        n = len(s)

        i = 0
        while i < n:
            if s[i] == "(":
                j = i
                while j < n and s[j] != ")":
                    j += 1
                word = s[i + 1: j]
                if word in mpp:
                    final.extend(mpp[word])
                else:
                    final.append("?")
                i = j + 1
            else:
                final.append(s[i])
                i += 1
        
        return "".join(final)
