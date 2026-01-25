class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:

        neg = [] #[num, idx]
        pos = deque()
        n = len(nums)
        for i, num in enumerate(nums):
            if num < 0:
                neg.append([num, i])
            else:
                pos.append([num, i])

        k = k % len(pos) if pos else 0

        for _ in range(k):
            pos.append(pos.popleft())

        final = []
        j = 0

        while pos and j < len(neg):
            curr = len(final)
            if neg[j][1] == curr:
                final.append(neg[j][0])
                j += 1
            else:
                final.append(pos.popleft()[0])

        while pos:
            final.append(pos.popleft()[0])

        while j < len(neg):
            final.append(neg[j][0])
            j += 1
        return final
            
                

        i = 0
        
        

        