class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        def neighbors(word):
            ans = []
            for i in range(len(word)):
                for ch in "ACGT":
                    new = word[:i] + ch + word[i+1:]
                    if new in bank:
                        ans.append(new)
            return ans
        
        q = deque()
        seen = set()

        q.append((startGene,0))
        seen.add(startGene)
        while q:
            word, steps = q.popleft()

            if word == endGene:
                return steps

            for nei in neighbors(word):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, steps +1))
        
        return -1

