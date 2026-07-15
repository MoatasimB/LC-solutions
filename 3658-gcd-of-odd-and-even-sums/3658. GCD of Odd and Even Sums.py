class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        

        totalS = (n * (n + 1)) // 2
        oddS = n*n
        evenS = n*n + n
        print(totalS, oddS, evenS)
        return math.gcd(oddS, evenS)