class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num == ".":
                    continue
                if num in rows[r] or num in cols[c] or num in box[(r//3,c//3)]:
                    print(num, r, c)
                    return False
                else:
                    rows[r].add(num)
                    cols[c].add(num)
                    box[(r//3,c//3)].add(num)
        return True

