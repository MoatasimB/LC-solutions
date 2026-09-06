class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.used = set()
        self.numbers = [i for i in range(maxNumbers)]

    def get(self) -> int:
        num = -1
        if self.numbers:
            num = self.numbers.pop()
            self.used.add(num)
        return num

    def check(self, number: int) -> bool:
        return number not in self.used
        

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)
            self.numbers.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)