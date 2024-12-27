class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:


        map = {}
        map2 = {}
        for ch in range(len(t)):
            map2[t[ch]] = map2.get(t[ch], 0) + 1

        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = t[i]
            else:
                if map[s[i]] != t[i]:
                    return False
            
        if len(map) != len(map2):
            return False
        return True
        