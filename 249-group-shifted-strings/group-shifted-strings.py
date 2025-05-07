class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        seen = set()

        counts = defaultdict(int)

        for word in strings:
            counts[word] += 1
        
        strings = set(strings)

        def getNei(word):
            neighbors = []
            for i in range(26):
                curr = []
                for ch in word:
                    ch_idx = ord(ch) - ord('a') # 0 .. 26
                    new_ch = chr((ch_idx + i) % 26 + ord('a'))
                    curr.append(new_ch)
                new_word = "".join(curr)
                if new_word in strings:
                    for _ in range(counts[new_word]):
                        neighbors.append(new_word)
                    seen.add(new_word)
            return neighbors
        
        dic = defaultdict(list)

        for word in strings:
            if word not in seen:
                neighbors = getNei(word)
                dic[word] = neighbors
        
        return list(dic.values())
