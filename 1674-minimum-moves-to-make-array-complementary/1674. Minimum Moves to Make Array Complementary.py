class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        sums = defaultdict(int)
        min_arr = []
        max_arr = []

        for i in range(n // 2):
            a = min(nums[i], nums[n - i - 1])
            b = max(nums[i], nums[n - i - 1])

            sums[a + b] += 1
            min_arr.append(a)
            max_arr.append(b)
        
        min_arr.sort()
        max_arr.sort()
        ans = n
        for c in range(2, 2 * limit + 1):
            #if c is less than or equal to a we must do 2 changes

            #if c is == a + b we don't do any changes

            #if c is greater than b + limit we need to do 2 changes
            pairs = n // 2
            pairs_equal = sums[c]
            pairs_less = pairs - bisect.bisect_left(min_arr, c)
            pairs_more = bisect.bisect_left(max_arr, c - limit)
            changes = pairs + pairs_less + pairs_more - pairs_equal
            ans = min(ans, changes)
        
        return ans

        
        
