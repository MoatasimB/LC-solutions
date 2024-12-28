class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = defaultdict(list)

        for i in range(len(strs)):
            key = [0] * 26
            for ch in strs[i]:
                key[ord(ch) - ord('a')] +=1
            
            mpp[tuple(key)].append(strs[i])
        ans = [val for val in mpp.values()]
        return ans