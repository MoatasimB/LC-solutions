class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mpp = defaultdict(int)

        for num in nums:
            mpp[num] += 1
        
        arr = list(mpp.keys())
        n = len(arr)
        
        def quickSelect(left, right):

            if left >= right:
                return
            
            rand_pivot = random.randint(left, right)

            piv_idx = partition(left, right, rand_pivot)

            if piv_idx > n - k:
                quickSelect(left, piv_idx - 1)
            elif piv_idx < n-k:
                quickSelect(piv_idx + 1, right)
            else:
                return
        
        def partition(left, right, pivot_index):


            val = mpp[arr[pivot_index]]

            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
            store_index = left
            for i in range(left, right):
                if mpp[arr[i]] < val:
                    arr[i], arr[store_index] = arr[store_index], arr[i]
                    store_index += 1
            
            arr[store_index], arr[right] = arr[right], arr[store_index]
            return store_index
        

        quickSelect(0, n - 1)

        return arr[n-k:]

