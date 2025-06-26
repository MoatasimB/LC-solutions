class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        mpp = defaultdict(int)
        ans = 0

        for i in range(len(time)):

            curr = (time[i] % 60)

            if ((60 - curr) % 60) in mpp:
                ans += mpp[(60 - curr) % 60]
            
            mpp[curr] += 1
        
        return ans