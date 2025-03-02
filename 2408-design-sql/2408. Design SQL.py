class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.names = names
        self.columns = columns
        self.name_to_col = {}
        self.tables = {}
        self.name_counters = {c:1 for c in names}
        for i in range(len(names)):
            self.name_to_col[names[i]] = columns[i]
            self.tables[names[i]] = {}

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.name_to_col or self.name_to_col[name] != len(row):
            return False
        id = self.name_counters[name]
        self.tables[name][id] = row
        self.name_counters[name] += 1
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.name_to_col or rowId not in self.tables[name]:
            return
        
        del self.tables[name][rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.name_to_col or rowId not in self.tables[name] or columnId > self.name_to_col[name]:
            return "<null>"
        
        return self.tables[name][rowId][columnId - 1]

    def exp(self, name: str) -> List[str]:
        if name not in self.name_to_col:
            return []
        
        ans = []
        
        for rowID, row in self.tables[name].items():
            ans.append(f"{rowID}," + ",".join(row))
        
        return ans
            
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)