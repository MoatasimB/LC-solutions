class Solution:
    def alienOrder(self, words: List[str]) -> str:
        inDeg = {c:0 for word in words for c in word}
        neighbors = {c:[] for word in words for c in word}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in neighbors[w1[j]]:
                        inDeg[w2[j]] += 1
                        neighbors[w1[j]].append(w2[j])
                    break

            
        q = deque()
        print(inDeg)
        print(neighbors)

        for k, v in inDeg.items():
            if v == 0:
                q.append(k)

        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for nei in neighbors[node]:
                inDeg[nei] -= 1
                if inDeg[nei] == 0:
                    q.append(nei)
                

        return "".join(ans) if sum(inDeg.values()) == 0 else ""