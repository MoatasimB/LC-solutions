class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        s = []
        l = []

        left = 0
        answer = 0
        for right in range(len(nums)):
            heapq.heappush(s, (nums[right], right))
            heapq.heappush(l, (-nums[right], right))

            diff = abs(s[0][0] + l[0][0])

            while diff > limit:

                left = min(s[0][1], l[0][1]) + 1

                while l[0][1] < left:
                    heapq.heappop(l)
                while s[0][1] < left:
                    heapq.heappop(s)
                # if nums[left] == s[0]:
                #     heapq.heappop(s)
                # elif nums[left] == -l[0]:
                #     heapq.heappop(l)

                
                # if len(s)==0 or len(l)==0:
                #     break
                # print(s)
                # print(l)
                diff = abs(s[0][0] + l[0][0])
                # left +=1
            
            answer = max(answer, right - left + 1)
 
        return answer