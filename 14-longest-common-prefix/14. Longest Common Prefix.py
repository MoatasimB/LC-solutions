class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        curr = []
        for i in range(len(strs[0])):

            for word in strs[1:]:
                if i == len(word) or strs[0][i] != word[i]:
                    return "".join(curr)
            
            curr.append(strs[0][i])
        
        return "".join(curr)
