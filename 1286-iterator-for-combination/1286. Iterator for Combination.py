class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.l = combinationLength
        self.all = []

        def dfs(i, curr):
            if len(curr) == self.l:
                self.all.append("".join(curr[:]))
                return
            if i == len(self.characters):
                return
            
            curr.append(self.characters[i])
            dfs(i+1, curr)
            curr.pop()

            dfs(i+1, curr)
        
        dfs(0, [])
        print(self.all)
        self.pos = 0

    def next(self) -> str:
        x = self.all[self.pos]
        self.pos +=1
        return x
        

    def hasNext(self) -> bool:
        if self.pos < len(self.all):
            return True
        return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()