class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        self.k = k
        class Node:
            def __init__(self):
                self.children = {}
                self.end = False
        
        class Trie:
            def __init__(self):
                self.root = Node()
            
            def add_word(self, word):
                curr = self.root

                for c in word:
                    if c not in curr.children:
                        curr.children[c] = Node()
                    curr = curr.children[c]
                curr.end = True
            

            def get_word(self,curr,word):
                nonlocal k
                if k == 0:
                    return []
                res = []
                if curr.end:
                    k -= 1
                    res.append(word)

                for i in range(26):
                    c = chr(ord('a') + i)

                    if c in curr.children:
                        res += self.get_word(curr.children[c], word + c)

                return res

        n = len(words)
        buckets = [[] for _ in range(n + 1)]

        freq = defaultdict(int)

        for word in words:
            freq[word] += 1
        
        for word, count in freq.items():
            if len(buckets[count]) == 0:
                buckets[count].append(Trie())
            buckets[count][0].add_word(word)

        ans = []

        for i in range(n, -1, -1):
            if k == 0:
                return ans
            if len(buckets[i]) == 1:
                t = buckets[i][0]
                ans.extend(t.get_word(t.root, ""))
        
        return ans


