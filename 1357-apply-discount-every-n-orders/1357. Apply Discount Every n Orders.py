class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.customer = 1
        self.discount = discount
        self.prices = {product:price for product, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0

        for j in range(len(product)):
            bill += self.prices[product[j]] * amount[j]

        if self.customer % self.n == 0:
            bill *= ((100 - self.discount) / 100)
        
        self.customer += 1
        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)