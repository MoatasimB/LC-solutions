class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        if not strs:
            return ""
        
        prefix = strs[0]

        for word in strs[1:]:
            
            j = 0
            while j < (min(len(word), len(prefix))):
                if word[j] != prefix[j]:
                    break
                j += 1
            
            prefix = word[:j]
        
        return prefix