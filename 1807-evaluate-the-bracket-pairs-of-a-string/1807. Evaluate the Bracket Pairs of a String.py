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
                start = i
                while i < n and s[i] != ")":
                    i += 1
                word = s[start + 1: i]
                if word in mpp:
                    final.extend(mpp[word])
                else:
                    final.append("?")
                
            else:
                final.append(s[i])
            i += 1
        
        return "".join(final)
