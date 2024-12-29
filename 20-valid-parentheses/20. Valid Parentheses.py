class Solution:
    def isValid(self, s: str) -> bool:
        answer= []
        for symbol in s:
            if symbol == "(" or symbol == "{" or symbol == "[":
                answer.append(symbol)
            elif symbol == ")":
                if answer and answer[-1] == "(":
                    answer.pop()
                else:
                    answer.append(symbol)
            elif symbol == "}":
                if answer and answer[-1] == "{":
                    answer.pop()
                else:
                    answer.append(symbol)
            elif symbol == "]":
                if answer and answer[-1] == "[":
                    answer.pop()
                else:
                    answer.append(symbol)

        if len(answer) == 0:
            return True
        else:
            return False