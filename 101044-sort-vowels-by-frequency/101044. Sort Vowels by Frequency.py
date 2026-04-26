class Solution:
    def sortVowels(self, s: str) -> str:

        freq = defaultdict(int)
        first = {}
        vowelPos = []

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            if ch in "aeiou":
                freq[ch] += 1
                vowelPos.append([i, ch])

        mpp = []
        for key, val in freq.items():
            mpp.append([key, val])
        mpp.sort(key = lambda x: (-x[1], first[x[0]]))

        # print(mpp)

        i = 0
        s_list = list(s)
        for j, ch in enumerate(s):
            if ch in "aeiou":
                currentCh, currCount = mpp[i]
                s_list[j] = currentCh
                mpp[i][1] -= 1
                
                if mpp[i][1] == 0:
                    i += 1

        return "".join(s_list)
                
            
                
        