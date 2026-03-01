class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        s = list(s)
        while s and s[-1] in "aeiou":
            s.pop()

        return "".join(s)