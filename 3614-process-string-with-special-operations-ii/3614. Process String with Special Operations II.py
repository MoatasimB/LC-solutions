class Solution:
    def processStr(self, s: str, k: int) -> str:
        
        _len = 0

        for ch in s:
            if ch == "%":
                continue
            elif ch == "#":
                _len *= 2
            elif ch == "*":
                if _len:
                    _len -= 1
            else:
                _len += 1
        print(_len)
        if _len <= k:
            return "."
        n = len(s)
        for i in range(n - 1, -1, -1):
            ch = s[i]
            if ch == "*":
                _len += 1
            elif ch == "%":
                k = _len - k - 1
            elif ch == "#":
                if k + 1 > (_len + 1) // 2:
                    k -= _len // 2
                _len = (_len + 1) // 2
            else:
                if k == _len - 1:
                    return ch
                else:
                    _len -= 1
        
        return "."

            
        # k = 3


        # dcddcd _len = 6
        #    ^
        