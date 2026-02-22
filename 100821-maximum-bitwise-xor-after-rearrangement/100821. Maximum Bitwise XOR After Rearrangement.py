class Solution:
    def maximumXor(self, s: str, t: str) -> str:

        freq = defaultdict(int)

        for ch in t:
            freq[ch] += 1
        ans = []
        for i in range(len(s)):
            if s[i] == "0":
                if freq["1"] > 0:
                    freq["1"] -= 1
                    ans.append("1")
                else:
                    freq["0"] -= 1
                    ans.append("0")
            else:
                if freq["0"] > 0:
                    freq["0"] -= 1
                    ans.append("1")
                else:
                    freq["1"] -= 1
                    ans.append("0")
        return "".join(ans)
                
            