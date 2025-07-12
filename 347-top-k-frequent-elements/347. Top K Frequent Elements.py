class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mpp = defaultdict(int)
        for num in nums:
            mpp[num] += 1

        arr = list(mpp.keys())
        n = len(arr)
        
        def quickSort(left, right):
            if left >= right:
                return 
            
            rand_pivot = random.randint(left, right)

            piv_idx = partition(left, right, rand_pivot)

            if piv_idx < n - k:
                quickSort(piv_idx + 1, right)
            elif piv_idx > n - k:
                quickSort(left, piv_idx - 1)
            else:
                return
        

        def partition(left, right, pivot_index):

            val = mpp[arr[pivot_index]]
            arr[right], arr[pivot_index] = arr[pivot_index],arr[right]

            store_idx = left

            for i in range(left, right):
                if mpp[arr[i]] < val:
                    arr[i], arr[store_idx] = arr[store_idx], arr[i]
                    store_idx += 1
            
            arr[store_idx], arr[right] = arr[right], arr[store_idx]

            return store_idx
        
        quickSort(0, n - 1)

        return arr[n-k:]