class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        graph = defaultdict(list)
        inDeg = {c:0 for word in words for c in word}
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]

            minLen = min(len(w1), len(w2))

            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    inDeg[w2[j]] +=1
                    break
        print(graph)
        print(inDeg)
        q = deque()

        for key, val in inDeg.items():
            if val == 0:
                q.append(key)
        
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)

            for nei in graph[node]:
                inDeg[nei] -= 1
                if inDeg[nei] == 0:
                    q.append(nei)
        
        return "".join(ans) if sum(inDeg.values()) == 0 else ""
