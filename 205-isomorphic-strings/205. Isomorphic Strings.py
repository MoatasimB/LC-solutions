class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}

        for i in range(len(s)):

            sch = s[i]
            tch = t[i]

            if s[i] not in mapping_s_t and t[i] not in mapping_t_s:
                mapping_s_t[s[i]] = t[i]
                mapping_t_s[t[i]] = s[i]
            else:
                if mapping_s_t.get(s[i]) != t[i] or mapping_t_s.get(t[i]) != s[i]:
                    return False
        return True
