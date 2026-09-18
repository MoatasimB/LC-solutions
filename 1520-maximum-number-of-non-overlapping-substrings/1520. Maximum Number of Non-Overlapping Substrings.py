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
        # substrings = list(substrings)
        substrings.sort(key=lambda x:(x[1], x[2]))
        ans = []
        
        for start, end, length in substrings:
            if not ans:
                ans.append([start, end])
            else:
                prevS, prevE = ans[-1]
                if start <= prevE:
                    continue
                ans.append([start, end])

        
        final = []
        for start, end in ans:
            final.append(s[start: end + 1])
        
        return final
