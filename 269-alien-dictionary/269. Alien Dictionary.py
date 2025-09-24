class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {ch : set() for word in words for ch in word}
        inDeg = {ch:0 for ch in graph.keys()}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            word1_len = len(word1)
            word2_len = len(word2)

            n= min(word1_len, word2_len)
            
            if word1[:n] == word2[:n] and word1_len > word2_len:
                return ""
            
            for ch in range(n):
                if word1[ch] != word2[ch]:
                    if word2[ch] not in graph[word1[ch]]:
                        graph[word1[ch]].add(word2[ch])
                        inDeg[word2[ch]] += 1
                    break

        q = deque()

        for ch, indeg in inDeg.items():
            if indeg == 0:
                q.append(ch)
        
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for nei in graph[node]:
                inDeg[nei] -= 1
                if inDeg[nei] == 0:
                    q.append(nei)

        return "".join(ans) if sum(inDeg.values()) == 0 else ""

