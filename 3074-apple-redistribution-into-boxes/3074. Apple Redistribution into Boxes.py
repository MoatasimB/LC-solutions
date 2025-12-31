class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        capacity.sort(reverse = True)

        total = sum(apple)
        ans = 0
        i = 0
        while i < len(capacity):
            total -= capacity[i]

            ans += 1

            if total <= 0:
                break
            
            i += 1
        
        return ans