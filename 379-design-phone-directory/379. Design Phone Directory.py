class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.free = [i for i in range(maxNumbers)]
        self.used = set()

    def get(self) -> int:
        if len(self.free) == 0:
            return -1
        x = self.free.pop()
        self.used.add(x)
        return x

    def check(self, number: int) -> bool:
        return number not in self.used
        

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)
            self.free.append(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)