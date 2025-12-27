class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        self.mpp = defaultdict(list)


        for word in strs:
            key = sorted(word)
            self.mpp[tuple(key)].append(word)
        

        return list(self.mpp.values())