class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        mpp = {}

        for key, val in knowledge:
            mpp[key] = val
        
        stack = []

        i = 0

        while i < len(s):
            if s[i] == "(":
                i += 1
                curr = []
                while i < len(s) and s[i] != ")":
                    curr.append(s[i])
                    i += 1
                word = "".join(curr)
                
                if word in mpp:
                    stack.append(mpp[word])
                else:
                    stack.append("?")

                i += 1
            else:
                stack.append(s[i])
                i += 1
        

        return "".join(stack)