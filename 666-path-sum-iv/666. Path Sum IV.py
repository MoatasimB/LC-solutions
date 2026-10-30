class Solution:
    def pathSum(self, nums: List[int]) -> int:
        

# ............1
# .......7.........1
# ....5
# .5



# 1 -> 1, 2
# 2 -> 3, 4
# 3 -> 5, 6
# 4 -> 7, 8

        nums.sort()
        mpp = {1: [1, 2], 2: [3, 4], 3: [5, 6], 4: [7, 8]}

    #child is at idx * 2 + 1, idx * 2 + 2, need to check whether child level = parent level + 1, and we can check if it 
        ans = 0
        def dfs(i, curr):

            nonlocal ans
            # if i == len(nums):
            #     nonlocal ans
            #     ans += curr
            #     return 
            n = str(nums[i])
            depth = int(n[0])
            pos = int(n[1])
            val = int(n[2])
            has_child = False
            for j in range(i + 1, len(nums)):
                child = str(nums[j])
                child_depth = int(child[0])
                child_pos = int(child[1])
                child_val = int(child[2])

                if child_depth > depth + 1:
                    break
                if child_depth == depth + 1 and child_pos in mpp[pos]:
                    #we are looking at the child
                    has_child = True
                    dfs(j, curr + val)
            
            if not has_child:
                ans += curr + val
                
            # print(i, curr)
            # #go left
            # left_child = i * 2 + 1
            # has_left = (left_child < len(nums) and int(str(nums[left_child])[0]) == depth + 1)
            # if has_left:
            #     dfs(left_child, curr + val)
            # #go right
            # right_child = i * 2 + 2
            # has_right = (right_child < len(nums) and int(str(nums[right_child])[0]) == depth + 1)
            # if has_right:
            #     dfs(right_child, curr + val)
            # if not has_left and not has_right:
            #     print(i, nums[i], curr)
            #     ans += (curr + val)
            # print(i, curr)
        dfs(0, 0)
        return ans


       

