class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        i = 0
        ans = 0
        while i < len(s):
            if i+1 >= len(s):
                ans += dic[s[i]]
                i+=1
                continue
            if s[i] == 'I' and s[i+1] == 'V':
                ans += 4
                i += 2
            elif s[i] == 'I' and s[i+1] == 'X':
                ans += 9
                i += 2
            elif s[i] == 'X' and s[i+1] == 'L':
                ans += 40
                i += 2
            elif s[i] == 'X' and s[i+1] == 'C':
                ans += 90
                i += 2
            elif s[i] == 'C' and s[i+1] == 'D':
                ans += 400
                i += 2
            elif s[i] == 'C' and s[i+1] == 'M':
                ans += 900
                i += 2
            else:
                ans += dic[s[i]]
                i+=1
        return ans

