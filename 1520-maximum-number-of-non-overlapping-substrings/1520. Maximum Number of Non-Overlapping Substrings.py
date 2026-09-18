class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        

        substrings = []
        n = len(s)
        first = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
        last = {ch: i for i, ch in enumerate(s)}

        for ch in first:
            begin = first[ch]
            end = last[ch]
            idx = begin
            while idx < end:
                letter = s[idx]
                end = max(end, last[letter])
                if first[letter] < begin:

                    begin = min(begin, first[letter])
                    idx = begin
                    continue

                idx += 1
            substrings.append((begin, end, end - begin + 1))
        
        substrings.append((0, n - 1, n))
        substrings.sort(key=lambda x:(x[1]))
        ans = []
        prevStart = -1
        prevEnd = -1
        for start, end, length in substrings:
            if not ans:
                ans.append(s[start: end + 1])
                prevStart = start
                prevEnd = end
            else:
                if start <= prevEnd:
                    continue
                ans.append(s[start: end + 1])
                prevStart = start
                prevEnd = end

        
        return ans