class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        unique = [element for element in count]
        n = len(unique)

        def partition(l, r, pivot):
            freq = count[unique[pivot]]
            unique[pivot], unique[r] = unique[r], unique[pivot]

            s = l
            for i in range(l, r):
                if count[unique[i]] < freq:
                    unique[s], unique[i] = unique[i], unique[s]
                    s += 1
            
            unique[r], unique[s] = unique[s], unique[r]
            return s

        def quickSelect(l, r):
            if l >= r: return

            possible_pivot = random.randint(l, r)

            pivot = partition(l, r, possible_pivot)

            if pivot == n - k:
                return
            elif pivot > n - k:
                quickSelect(l, pivot - 1)
            else:
                quickSelect(pivot + 1, r)
        
        quickSelect(0, n - 1)

        return unique[n-k: ]

        