class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowerCaseLast = {}
        upperCaseFirst = {}
        n = len(word)
        for i in range(n):
            if word[i] in "abcdefghijklmnopqrstuvwxyz":
                lowerCaseLast[word[i]] = i
            else:
                if word[i] not in upperCaseFirst:
                    upperCaseFirst[word[i]] = i
        
        ans = 0
        for key, idx in lowerCaseLast.items():
            if key.upper() in upperCaseFirst:
                ans += (idx < upperCaseFirst[key.upper()])
        
        return ans
