class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        bank = set(bank)
        
        def neighbors(gene):
            ans = []
            for i in range(8):
                char = gene[i]
                for ch in "ACTG":
                    stringGene = "".join(gene[:i] + ch + gene[i+1:])
                    # ans.append(stringGene)
                    ans.append(gene[:i] + ch + gene[i+1:])

            

            return ans
        

        q = deque([(startGene,0)])
        seen = {startGene}
        
        while q:
            currGene, steps = q.popleft()
            
            if currGene == endGene:
                return steps
            
            for neighbor in neighbors(currGene):
                if neighbor in bank and neighbor not in seen:
                    seen.add(neighbor)
                    q.append((neighbor, steps + 1))
            
        
        return -1 
            
                
        