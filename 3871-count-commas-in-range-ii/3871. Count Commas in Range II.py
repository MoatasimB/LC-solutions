class Solution:
    def countCommas(self, n: int) -> int:
        
        if n < 1000:
            return 0
        if n == 10**15:
            return 5 + 4*(998999999999999 + 1) + 3*(998999999999 + 1) + 2*(998999999 + 1) + 998999 + 1
        one = n - 1000 + 1
        if n < 10**6:
            return one
        two = 2 * ((n - 10**6) + 1) + 998999 + 1
      
        if n < 10**9:
            return two
        three = 3 * (n - 10**9 + 1) + 2*(998999999 + 1) + 998999 + 1
        if n < 10**12:
            return three
        four = 4 * (n - 10**12 + 1) + 3*(998999999999 + 1) + 2*(998999999 + 1) + 998999 + 1
        return four
        #1 comma for 1,000 - 999,999
        #2 comma for 1,000,000 - 999,999,999
        #3 comma for 1,000,000,000 - 999,999,999,999
        #4 comma for 1,000,000,000,000 - 999,999,999,999,999
        #5 comma for 1,000,000,000,000,000