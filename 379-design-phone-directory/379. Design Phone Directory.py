class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.free = [i for i in range(maxNumbers)]
        self.used = [False] * maxNumbers

    def get(self) -> int:
        if len(self.free) == 0:
            return -1
        x = self.free.pop()
        self.used[x] = True
        return x

    def check(self, number: int) -> bool:
        return not self.used[number]
        

    def release(self, number: int) -> None:
        if self.used[number]:
            self.used[number] = False
            self.free.append(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)