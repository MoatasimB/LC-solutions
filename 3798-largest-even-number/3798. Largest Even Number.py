class Solution:
    def largestEven(self, s: str) -> str:

        lst = list(s)

        while lst and int(lst[-1]) % 2 == 1:
            lst.pop()

        if lst:
            return "".join(lst)
        return ""
        