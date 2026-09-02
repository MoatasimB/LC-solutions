class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.o_set = set()
        self.x_set = set()

    def move(self, row: int, col: int, player: int) -> int:
        player_set = self.x_set if player == 1 else self.o_set
        player_set.add((row, col))
        return self.check(row, col, player)
        

        
    
    def check(self, row, col, player):
        player_set = self.x_set if player == 1 else self.o_set
        player_num = player
        #check neg diagonal
        x, y = row - 1, col - 1
        count = 1
        while (x, y) in player_set:
            x -= 1
            y -= 1
            count += 1
        x, y = row + 1, col + 1
        while (x, y) in player_set:
            x += 1
            y += 1
            count += 1
        if count == self.n:
            return player_num

        #check pos diagonal

        x, y = row - 1, col + 1
        count = 1
        while (x, y) in player_set:
            x -= 1
            y += 1
            count += 1
        x, y = row + 1, col - 1
        while (x, y) in player_set:
            x += 1
            y -= 1
            count += 1
        if count == self.n:
            return player_num
        #check horizontal
        x, y = row, col - 1

        count = 1
        while (x, y) in player_set:
            y -= 1
            count += 1
        x, y = row, col + 1
        while (x, y) in player_set:
            y += 1
            count += 1
        if count == self.n:
            return player_num


        #check vertical
        x, y = row - 1, col
        count = 1
        while (x, y) in player_set:
            x -= 1
            count += 1
        x, y = row + 1, col
        while (x, y) in player_set:
            x += 1
            count += 1
        if count == self.n:
            return player_num
        
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)