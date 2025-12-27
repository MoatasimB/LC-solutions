class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        self.mpp = defaultdict(list)

        def makeKey(word):
            lst = [0] * 26
            for ch in word:
                lst[ord(ch) - ord('a')] += 1
            
            return lst


        for word in strs:
            key = makeKey(word)
            self.mpp[tuple(key)].append(word)
        

        return list(self.mpp.values())