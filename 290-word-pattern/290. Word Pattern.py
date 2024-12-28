class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        mappings = {}
        s  = s.split()
        if len(pattern) != len(s):
            return False
        for i, ch in enumerate(pattern):
            if ch in mappings:
                if mappings[ch] != s[i]:
                    print(mappings, ch, s[i])
                    return False
            else:
                mappings[ch] = s[i]
        return len(mappings) == len(set(mappings.values()))