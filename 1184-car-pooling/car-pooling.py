class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # trips.sort(key = lambda x : x[1])

        arr = [0] * 1001

        for num, start, end in trips:
            if num > capacity:
                return False
            arr[start] += num
            if end < len(arr):
                arr[end] -= num
        
        for i in range(1, len(arr)):
            arr[i] = arr[i] + arr[i-1]
            if arr[i] > capacity:
                return False
        
        return True