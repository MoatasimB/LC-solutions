class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sum = defaultdict(int)


        for i in range(1, n + 1):

            curr = i
            d_sum = 0
            while curr:
                d_sum += curr % 10
                curr = curr // 10
            
            digit_sum[d_sum] += 1
        
        ans = 0
        m_max = float('-inf')
        for key, val in digit_sum.items():

            if val > m_max:
                ans =1
                m_max = val
            elif val == m_max:
                ans += 1
        
        return ans

