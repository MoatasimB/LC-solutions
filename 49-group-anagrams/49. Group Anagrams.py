class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #placeholders for all letters
            for ch in s:
                count[ord(ch) - ord("a")] +=1 #creates a unique list w freq of all the characters in the word
            res[tuple(count)].append(s) #we use that unique list as a key because all anagrams will have the same unique list and then we append that word
        return res.values()


        # # from collections import defaultdict
        # anagrams = defaultdict(list)

        # for word in strs:
        #     key = "".join(sorted(word))
        #     anagrams[key].append(word)

        # return anagrams.values()