class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_l = len(words[0])

        counts = defaultdict(int)
        for word in words:
            counts[word] += 1
        
        ans = []
        for i in range(n - (k*word_l) + 1):
            need = k
            seen = defaultdict(int)
            for j in range(i, i + k*word_l, word_l):
                string = s[j: j+ word_l]
                if string in counts:
                    seen[string] += 1
                    if seen[string] <= counts[string]:
                        need -= 1
                        if need == 0:
                            ans.append(i)
                            break
                else:
                    break
        return ans


            