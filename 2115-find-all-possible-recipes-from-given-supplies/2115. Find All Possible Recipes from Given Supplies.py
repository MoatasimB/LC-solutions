class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        supplies = set(supplies)
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for supply in supplies:
            indeg[supply] = 0
        
        for i, item in enumerate(recipes):
            for part in ingredients[i]:
                graph[part].append(item)
                indeg[item] += 1
        
        q = deque()
        for part in indeg:
            if indeg[part] == 0:
                q.append(part)
        
        ans = []

        while q:
            part = q.popleft()
            if part not in supplies:
                ans.append(part)

            for nei in graph[part]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return ans

        
        
        
        
        
        
        # def canMake(idx, item):
        #     if item in supplies:
        #         supplies.add(item)
        #         return True
        #     elif item in recipes:
        #         for i, part in enumerate(ingredients[idx]):
        #             if not canMake(i, part):
        #                 return False
        #         supplies.add(item)
        #         return True
            
        #     return False

        # ans = []
        # for i, recipe in enumerate(recipes):
        #     if canMake(i, recipe):
        #         supplies.add(recipe)
        #         ans.append(recipe)
        
        # return ans
