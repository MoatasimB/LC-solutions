class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        
        # lights = lights.sort(key = lambda x : x[0])
        
        # diff_a = [0] * (lights[-1][0] - lights[0][0])

        mpp = defaultdict(int)

        for pos, r in lights:
            mpp[pos - r] += 1
            mpp[pos + r + 1] -= 1

        ans = float("-inf")
        location = 0
        curr = 0
        for k in sorted(mpp.keys()):
            curr += mpp[k]

            if ans < curr:
                ans = curr
                location = k
        
        return location


