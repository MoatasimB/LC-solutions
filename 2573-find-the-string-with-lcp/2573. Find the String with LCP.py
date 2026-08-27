class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        
        n = len(lcp)
        curr_chr = ord('a')
        word = [""] * n

        for i in range(n):
            if not word[i]:
                if curr_chr > ord("z"):
                    return ""
                word[i] = chr(curr_chr)

                for j in range(i + 1, n):
                    if lcp[i][j] > 0:
                        word[j] = chr(curr_chr)
                curr_chr += 1
        

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j] > 0:
                        return ""
                else:
                    if (i == n - 1 or j == n - 1):
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""
        
        return "".join(word)