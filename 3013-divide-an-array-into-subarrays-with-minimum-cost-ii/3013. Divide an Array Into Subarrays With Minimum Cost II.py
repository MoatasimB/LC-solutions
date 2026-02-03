class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        
        class Container:
            def __init__(self, k):
                self.k = k
                self.low = SortedList()
                self.rest = SortedList()
                self.sm = 0
            
            def balance(self):
                while len(self.low) < self.k and self.rest:
                    val = self.rest[0] 
                    self.rest.remove(val)
                    self.low.add(val)
                    self.sm += val
                while len(self.low) > self.k:
                    val = self.low[-1]
                    self.low.remove(val)
                    self.rest.add(val)
                    self.sm -= val
            
            def add(self, val):
                if self.rest and val >= self.rest[0]:
                    self.rest.add(val)
                else:
                    self.low.add(val)
                    self.sm += val
                self.balance()
            
            def remove(self, val):
                if val in self.rest:
                    self.rest.remove(val)
                else:
                    self.low.remove(val)
                    self.sm -= val
                self.balance()
            
            def getSum(self):
                return self.sm
        n = len(nums)
        cont = Container(k - 2)
        for i in range(1, k - 1):
            cont.add(nums[i])
        
        ans = cont.getSum() + nums[k - 1]

        for i in range(k, n):
            j = i - dist - 1
            if j > 0:
                cont.remove(nums[j])
            cont.add(nums[i - 1])

            ans = min(ans, cont.getSum() + nums[i])
        
        return ans + nums[0]