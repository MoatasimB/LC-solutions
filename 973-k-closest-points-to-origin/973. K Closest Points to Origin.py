class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        distances = {}

        for i in range(len(points)):
            x, y = points[i]

            distances[i] = x**2 + y**2

        arr = list(distances.keys())
        
        def quickSelect(left, right, k):

            if left == right:
                return
            
            idx = random.randint(left, right)

            pivot_idx = partition(left, right, idx)

            if pivot_idx < k:
                quickSelect(pivot_idx + 1, right, k)
            elif pivot_idx > k:
                quickSelect(left, pivot_idx - 1, k)
            else:
                return
        
        def partition(left, right, p_idx):

            dist = distances[arr[p_idx]]

            arr[right], arr[p_idx] = arr[p_idx], arr[right]

            store_idx = left

            for i in range(left, right):
                if distances[arr[i]] < dist:
                    arr[store_idx], arr[i] = arr[i], arr[store_idx]
                    store_idx += 1
            
            arr[store_idx], arr[right] = arr[right], arr[store_idx]

            return store_idx
        

        n = len(arr)

        quickSelect(0, n - 1, k)

        orig = [points[idx] for idx in arr]
        return orig[:k]