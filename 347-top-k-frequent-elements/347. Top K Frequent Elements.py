class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1
        
        unique = list(counts.keys())

        n = len(unique)
        def quickselect(left, right):
            if left >= right:
                return
            
            p = random.randint(left, right)
            
            pivot = quicksort(left, right, p)
            
            if pivot == n - k:
                return 
            elif pivot < n - k:
                quickselect(pivot + 1, right)
            else:
                quickselect(left, pivot - 1)
        
        
        def quicksort(left, right, p):

            freq = counts[unique[p]]

            unique[p], unique[right] = unique[right], unique[p]

            curr = left

            for i in range(left, right):
                if counts[unique[i]] < freq:
                    unique[i], unique[curr] = unique[curr], unique[i]
                    curr += 1

            unique[curr], unique[right] = unique[right], unique[curr]

            return curr


        quickselect(0, n - 1)

        return unique[n - k: ]
            