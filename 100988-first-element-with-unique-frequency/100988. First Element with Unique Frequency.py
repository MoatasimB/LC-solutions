class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1


        freqCount = defaultdict(list)

        for k, v in freq.items():
            freqCount[v].append(k)

        for num in nums:
            if len(freqCount[freq[num]]) == 1:
                return num

        return -1