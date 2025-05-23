class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        mpp = [None] * ((n**2) + 1)
        label = 1
        columns = list(range(0,n))
        front = True
        for row in range(n-1, -1, -1):
            if front:
                for col in columns:
                    mpp[label] = (row ,col)
                    label +=1
            else:
                for col in columns[::-1]:
                    mpp[label] = (row ,col)
                    label +=1
            front = not front
            # columns.reverse()
        
        q = deque()
        q.append((1, 0))
        seen = set()
        seen.add(1)
        
        while q:
            sq, moves = q.popleft()
            if sq == n**2:
                return moves

            for nextSq in range(sq + 1, min(sq + 6, n*n) + 1):
                r,c = mpp[nextSq]
                if nextSq not in seen:
                    seen.add(nextSq)
                    if board[r][c] != -1:
                        q.append((board[r][c], moves +1))
                    else:
                        q.append((nextSq, moves + 1))
        
        return -1
