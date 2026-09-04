class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food_ptr = 0
        self.food = food
        self.snake_head = [0, 0]
        self.snake_body = deque() # head <------- tail
        self.dirs = {"U" : (-1,0), "D": (1,0), "L": (0, -1), "R":(0,1)}
        self.score = 0
    def valid(self, r, c):
        return 0 <= r < self.height and 0 <= c < self.width

    def move(self, direction: str) -> int:
        food_pos = self.food[self.food_ptr] if self.food_ptr < len(self.food) else None
        curr_pos = self.snake_head
        dx, dy = self.dirs[direction]
        nr, nc = curr_pos[0] + dx, curr_pos[1] + dy
        if not self.valid(nr, nc):
            return -1
        self.snake_body.appendleft([curr_pos[0], curr_pos[1]])

        if food_pos == [nr, nc]:
            self.score += 1
            self.food_ptr += 1

        else:
            if self.snake_body:
                self.snake_body.pop()
        

        if [nr, nc] in self.snake_body:
            return -1
        self.snake_head = [nr, nc]
        return self.score

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)


# F _ _ 

# B _ _ 

# S _ _ 

#  B S

#  B B 