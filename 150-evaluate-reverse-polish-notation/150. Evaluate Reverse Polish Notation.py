class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for i in range(len(tokens)):
            if tokens[i] in "+/*-":
                secondNum = s.pop()
                firstNum = s.pop()
                if tokens[i] == '+':
                    s.append(firstNum + secondNum)
                elif tokens[i] == '*':
                    s.append(firstNum * secondNum)
                if tokens[i] == '-':
                    s.append(firstNum - secondNum)
                if tokens[i] == '/':
                    s.append(int(firstNum / secondNum))
            else:
                s.append(int(tokens[i]))
        return s[0]