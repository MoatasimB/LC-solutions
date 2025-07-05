class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mpp = defaultdict(int)

        for num in nums:
            mpp[num] += 1
        
        arr = list(mpp.keys())
        
        
        def quickSelect(left, right, kth):

            if left == right:
                return
            
            index = random.randint(left, right)

            pivot_index = partition(left, right, index)

            if pivot_index > kth:
                quickSelect(left, pivot_index - 1, kth)
            elif pivot_index < kth:
                quickSelect(pivot_index + 1, right, kth)
            else:
                return
        
        def partition(left, right, p_idx):

            #move piv to end

            freq = mpp[arr[p_idx]]

            arr[p_idx], arr[right] = arr[right], arr[p_idx]
            store_index = left
            for i in range(left, right):
                if mpp[arr[i]] < freq:
                    arr[i], arr[store_index] = arr[store_index], arr[i]
                    store_index += 1
            
            arr[store_index], arr[right] = arr[right], arr[store_index]
            return store_index
        

        quickSelect(0, len(arr) - 1, len(arr) - k)

        return arr[len(arr)-k:]

