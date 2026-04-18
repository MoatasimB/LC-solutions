class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        n = len(nums)
        mpp = defaultdict(list)

        

        def rev(num):
            str_num = list(str(num))
            m = len(str_num)
            l = 0
            r = m - 1

            while l < r:
                str_num[l], str_num[r] = str_num[r], str_num[l]
                l += 1
                r -= 1
            
            i = 0
            while str_num[i] == "0":
                i += 1
            
            return int("".join(str_num[i:]))

        mpp = defaultdict(list)
        rev_nums = []
        for i in range(n):
            rev_nums.append(rev(nums[i]))
            mpp[nums[i]].append(i)
        
        min_dist = float("inf")

        def find_closest_idx(lst, idx):
            l = 0
            r = len(lst) - 1
            ans = None
            while l <= r:
                mid = (l + r) // 2

                if lst[mid] > idx:
                    ans = lst[mid]
                    r = mid - 1
                else:
                    l = mid + 1
            return ans



        for i in range(n):
            curr = nums[i]
            rev_num = rev_nums[i]

            lst = mpp[rev_num]
            closest_idx = find_closest_idx(lst, i)
            # print(i, closest_idx, mpp, lst)
            if closest_idx == i or closest_idx == None:
                continue
            min_dist = min(min_dist, abs(closest_idx - i))
        
        return min_dist if min_dist != float("inf") else -1
