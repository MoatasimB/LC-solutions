class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def count(l, r, mid):
            arr_size = mid - l + 1
            # print(nums[l : mid + 1], nums[mid + 1: r + 1])
            i = l
            j = mid + 1
            ans = 0
            while i <= mid and j <= r:
                
                if nums[i] > 2 * nums[j]:
                    # print(i, j, nums[i], nums[j], arr_size, l)

                    ans += arr_size - (i - l)
                    j += 1
                else:
                    i += 1
            
            
            return ans

        def merge(l, r, mid):
            ans = count(l, r, mid)
            i = l
            j = mid + 1

            temp = []
            while i <= mid and j <= r:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            while i <= mid:
                temp.append(nums[i])
                i += 1
            
            while j <= r:
                temp.append(nums[j])
                j += 1
            
            for i in range(l, r + 1):
                nums[i] = temp[i - l]

            return ans

        def mergesort(l, r):
            if l >= r:
                return 0

            count = 0
            mid = (l + r) // 2
            count += mergesort(l, mid)
            count += mergesort(mid + 1, r)
            count += merge(l, r, mid)
            return count
        
        return mergesort(0, len(nums) - 1)

        